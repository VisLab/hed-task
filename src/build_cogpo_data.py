"""Recompute data/cogpo_summary.json from the .cog_data/cogpo/ archive.

`.cog_data/cogpo/` is a byte-exact archive of CogPO, the Cognitive Paradigm Ontology,
written by `src/fetch_cogpo_data.py` and untracked. This script reads it and writes a
JSON summary that the documentation generators and the mapping builder consume, so that
`python src/generate_docs.py` and the CI docs build need only the committed summary,
never the archive.

Run it by hand whenever the archive is refreshed:

    python src/fetch_cogpo_data.py       # refresh .cog_data/cogpo/
    python src/build_cogpo_data.py       # recompute data/cogpo_summary.json

Expected archive layout::

    <archive>/MANIFEST.json                provenance for every stored response
    <archive>/owl/CogPOver1.owl            the ontology (RDF/XML)
    <archive>/wiki/pages/<title>.wiki      raw wikitext of one wiki term page

The OWL file is the ontology of record. The wiki is read alongside it because it
carries terms the OWL release does not (the four Stimulus Role values, a Delayed Match
To Sample paradigm) and a later curation pass (2011 against the OWL's 2010), and the
summary reports the two against each other.

What is derived here, and nowhere else:

- Each class's `id` is the last segment of its IRI, percent-decoded: `COGPO_00092` for
  most CogPO terms, `Button Press` or `Naming_(Overt)_Paradigm` for the 34 classes whose
  IRI is a name rather than a number, `FMA_9712` for body parts.
- Definitions are kept verbatim except for one export artifact: some arrive wrapped in
  CSV-style double quotes with inner quotes doubled. Those are unwrapped, and the count
  is reported under `hygiene`.
- An explicit stimulus's `stimulus_modality` is read from its `has_stimulus_modality`
  restriction; a union filler (words may be visual or auditory) gives several values.
- Response Modality classes are Foundational Model of Anatomy (FMA) ids with no label in
  the OWL. Their labels come from `FMA_LABELS`, checked against the EBI Ontology Lookup
  Service on 2026-09-22.

This module reads the archive but never rewrites it.
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

DEFAULT_ARCHIVE = Path(__file__).parent.parent / ".cog_data" / "cogpo"
OWL_FILE = "CogPOver1.owl"

OWL = "{http://www.w3.org/2002/07/owl#}"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
RDFS = "{http://www.w3.org/2000/01/rdf-schema#}"
OBO = "{http://purl.obolibrary.org/obo/}"
DC = "{http://purl.org/dc/elements/1.1/}"

# IAO annotation properties used by CogPO, by their meaning.
ANNOTATIONS = {
    "definition": OBO + "IAO_0000115",
    "definition_sources": OBO + "IAO_0000119",
    "editor_notes": OBO + "IAO_0000116",
    "curation_status": OBO + "IAO_0000114",
    "term_editor": OBO + "IAO_0000117",
    "date": DC + "date",
    "source": DC + "source",
    "comments": RDFS + "comment",
}

# The roots of the vocabularies the comparison uses, by OWL label. `kind` is the name
# the summary and the mapping tables use for the branch.
BRANCHES = [
    ("paradigm", "Behavioral Experimental Paradigm"),
    ("condition", "Behavioral Experimental Paradigm Condition"),
    ("stimulus_modality", "Stimulus Modality"),
    ("explicit_stimulus", "Explicit Stimulus"),
    ("implicit_stimulus", "Implicit Stimulus"),
    ("stimulus_role", "Stimulus role"),
    ("response_modality", "Response Modality"),
    ("overt_response", "Overt Response"),
    ("covert_response", "Covert Response"),
    ("response_role", "Response role"),
    ("instructions", "Instructions"),
]
DIMENSIONS = [kind for kind, _ in BRANCHES if kind not in ("paradigm", "condition")]

# Labels for the FMA body-part classes, which the OWL leaves unlabeled. Checked against
# the EBI Ontology Lookup Service (ols4, ontology `fma`) on 2026-09-22.
FMA_LABELS = {
    "FMA_24728": "Face",
    "FMA_24890": "Arm",
    "FMA_24979": "Leg",
    "FMA_25202": "Shoulder",
    "FMA_9578": "Pelvis",
    "FMA_9664": "Foot",
    "FMA_9712": "Hand",
    "FMA_49184": "Mouth",
}

# Wiki title of the page whose Parent Entity field names each dimension root.
WIKI_PARENTS = {
    "stimulus_modality": "Stimulus Modality",
    "explicit_stimulus": "Explicit Stimulus",
    "implicit_stimulus": "Implicit Stimulus",
    "stimulus_role": "Stimulus Role",
    "response_modality": "Response Modality",
    "overt_response": "Overt Response",
    "covert_response": "Covert Response",
    "response_role": "Response Role",
    "instructions": "Instructions",
}

_CSV_QUOTED = re.compile(r'^"(.*)"$', re.DOTALL)
_YEAR = re.compile(r"(?:^|\D)(20\d\d)(?:\D|$)|(?:^|\D)(\d\d)$")
_TEMPLATE_FIELD = re.compile(r"^\|\s*([^=\n]+?)\s*=\s*(.*?)(?=^\||^\}\})", re.M | re.S)
_WIKI_LINK = re.compile(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]")
_EXTERNAL_LINK = re.compile(r"\[(https?://\S+)(?:\s[^\]]*)?\]")


# ---------------------------------------------------------------------------
# OWL
# ---------------------------------------------------------------------------


def short_id(iri: str) -> str:
    """Return the last segment of an IRI, percent-decoded: `COGPO_00092`, `Button Press`."""
    return urllib.parse.unquote(re.sub(r"^.*[#/]", "", iri))


def _texts(element: ET.Element, tag: str) -> list[str]:
    return [(child.text or "").strip() for child in element.findall(tag) if (child.text or "").strip()]


def _clean_definition(text: str) -> tuple[str, bool]:
    """Unwrap a CSV-quoted definition. Returns (text, was_quoted)."""
    match = _CSV_QUOTED.match(text)
    if not match:
        return text, False
    return match.group(1).replace('""', '"').strip(), True


def _year(text: str) -> str:
    """Normalize the OWL's mixed date strings ('14 DEC 2010', '17-Aug-10') to a year."""
    match = _YEAR.search(text)
    if not match:
        return "(none)" if not text else "(unparsed)"
    return match.group(1) or ("20" + match.group(2))


def load_owl(path: Path) -> dict:
    """Parse the OWL file into classes, properties, individuals and axioms."""
    root = ET.fromstring(path.read_bytes())

    classes: dict[str, dict] = {}
    restrictions: list[dict] = []
    for element in root.findall(OWL + "Class"):
        iri = element.get(RDF + "about") or element.get(RDF + "ID") or ""
        label = (element.findtext(RDFS + "label") or "").strip()
        parents: list[str] = []
        for sub in element.findall(RDFS + "subClassOf"):
            target = sub.get(RDF + "resource")
            if target:
                parents.append(target)
                continue
            restriction = sub.find(OWL + "Restriction")
            if restriction is None:
                continue
            on_property = restriction.find(OWL + "onProperty")
            fillers: list[str] = []
            filler_kind = None
            for child in restriction:
                if child.tag == OWL + "onProperty":
                    continue
                filler_kind = child.tag.replace(OWL, "")
                if child.get(RDF + "resource"):
                    fillers.append(child.get(RDF + "resource"))
                else:
                    # A nested anonymous class, in practice `unionOf` two modalities
                    # (words may be visual or auditory). Keep every member.
                    fillers.extend(
                        member.get(RDF + "about") for member in child.iter(RDF + "Description") if member.get(RDF + "about")
                    )
            restrictions.append(
                {
                    "class": iri,
                    "property": on_property.get(RDF + "resource") if on_property is not None else None,
                    "kind": filler_kind,
                    "fillers": fillers,
                }
            )
        definition_raw = (element.findtext(ANNOTATIONS["definition"]) or "").strip()
        definition, quoted = _clean_definition(definition_raw)
        classes[iri] = {
            "iri": iri,
            "id": short_id(iri),
            "label": label,
            "parents": parents,
            "definition": definition,
            "definition_csv_quoted": quoted,
            "definition_sources": _texts(element, ANNOTATIONS["definition_sources"]),
            "editor_notes": _texts(element, ANNOTATIONS["editor_notes"]),
            "comments": _texts(element, ANNOTATIONS["comments"]),
            "curation_status": (element.findtext(ANNOTATIONS["curation_status"]) or "").strip(),
            "date": (element.findtext(ANNOTATIONS["date"]) or "").strip(),
            "source": _texts(element, ANNOTATIONS["source"]),
            "term_editor": (element.findtext(ANNOTATIONS["term_editor"]) or "").strip(),
            "equivalent_class": element.find(OWL + "equivalentClass") is not None,
        }

    properties = []
    for element in root.findall(OWL + "ObjectProperty"):
        iri = element.get(RDF + "about") or ""
        domain = element.find(RDFS + "domain")
        range_ = element.find(RDFS + "range")
        parent = element.find(RDFS + "subPropertyOf")
        properties.append(
            {
                "iri": iri,
                "id": short_id(iri),
                "label": (element.findtext(RDFS + "label") or "").strip(),
                "domain": domain.get(RDF + "resource") if domain is not None else None,
                "range": range_.get(RDF + "resource") if range_ is not None else None,
                "parent": parent.get(RDF + "resource") if parent is not None else None,
            }
        )

    individuals = []
    for element in root:
        if element.tag in (OWL + "Class", OWL + "ObjectProperty", OWL + "AnnotationProperty", OWL + "Ontology"):
            continue
        about = element.get(RDF + "about")
        if not about:
            continue
        types = [t.get(RDF + "resource") for t in element.findall(RDF + "type")]
        if element.tag != OWL + "Thing":
            types.append(element.tag[1:].replace("}", ""))
        individuals.append(
            {
                "id": short_id(about),
                "label": (element.findtext(RDFS + "label") or "").strip(),
                "types": [short_id(t) for t in types if t and not t.endswith("Thing")],
            }
        )

    disjoint = sum(
        1
        for element in root.findall(RDF + "Description")
        if any((t.get(RDF + "resource") or "").endswith("AllDisjointClasses") for t in element.findall(RDF + "type"))
    )

    ontology = root.find(OWL + "Ontology")
    imports = []
    if ontology is not None:
        imports = [i.get(RDF + "resource") for i in ontology.findall(OWL + "imports") if i.get(RDF + "resource")]

    return {
        "classes": classes,
        "restrictions": restrictions,
        "properties": properties,
        "annotation_properties": len(root.findall(OWL + "AnnotationProperty")),
        "individuals": individuals,
        "disjoint_axioms": disjoint,
        "imports": imports,
    }


# ---------------------------------------------------------------------------
# Wiki
# ---------------------------------------------------------------------------


def _strip_wiki_markup(text: str) -> str:
    text = _WIKI_LINK.sub(r"\1", text)
    text = _EXTERNAL_LINK.sub(r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def load_wiki(pages_dir: Path) -> dict[str, dict]:
    """Parse every archived wiki page into its template fields, keyed by page title.

    A term page is one that uses `Condition Template`. Pages without the template (the
    BFO upper classes, the body parts, the project pages) are kept with empty fields so
    the inventory can count them, and `is_term` says which is which.
    """
    pages: dict[str, dict] = {}
    if not pages_dir.exists():
        return pages
    for file in sorted(pages_dir.glob("*.wiki")):
        title = urllib.parse.unquote(file.stem)
        text = file.read_text(encoding="utf-8")
        fields: dict[str, str] = {}
        if "{{Condition Template" in text:
            body = text[text.index("{{Condition Template") :]
            for key, value in _TEMPLATE_FIELD.findall(body + "\n}}"):
                fields[key.strip()] = value.strip()
        definition = fields.get("Definition", "")
        pages[title] = {
            "title": title,
            "name": title.replace("_", " "),
            "is_term": bool(fields),
            "definition": _strip_wiki_markup(definition),
            "definition_external_links": _EXTERNAL_LINK.findall(definition)
            + re.findall(r"(?<!\[)https?://\S+", _WIKI_LINK.sub("", definition)),
            "definition_source": _strip_wiki_markup(fields.get("Definition Source", "")),
            "parent": _strip_wiki_markup(fields.get("Parent Entity", "")),
            "created": fields.get("Created Date", "").strip(),
            "curator": fields.get("Curator", "").strip(),
            "curation_status": fields.get("Curation Status", "").strip(),
            "uri": _strip_wiki_markup(fields.get("URI", "")),
            "example": _strip_wiki_markup(fields.get("Example", "")),
            "logical_restrictions": _strip_wiki_markup(fields.get("Logical Restrictions", "")),
        }
    return pages


def _norm(name: str) -> str:
    """Normalize a label for matching OWL against wiki.

    The wiki cannot have a slash in a title, so it writes `Monitor or Discrimination`
    where the OWL label says `Monitor/Discrimination`; both normalize to the same key.
    """
    text = name.replace("_", " ").replace("/", " or ")
    return re.sub(r"\s+", " ", text).strip().lower()


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------


def build(archive: Path) -> dict:
    owl_path = archive / "owl" / OWL_FILE
    if not owl_path.exists():
        raise SystemExit(f"Missing {owl_path}. Run src/fetch_cogpo_data.py first.")
    owl = load_owl(owl_path)
    classes = owl["classes"]
    wiki = load_wiki(archive / "wiki" / "pages")

    manifest_path = archive / "MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    owl_entry = manifest.get("owl", {}).get(OWL_FILE, {})

    by_label = {c["label"]: iri for iri, c in classes.items() if c["label"]}
    children: dict[str, list[str]] = collections.defaultdict(list)
    for iri, c in classes.items():
        for parent in c["parents"]:
            children[parent].append(iri)

    def label_of(iri: str | None) -> str:
        if not iri:
            return ""
        c = classes.get(iri)
        if c is None:
            return short_id(iri)
        return c["label"] or FMA_LABELS.get(c["id"], "") or c["id"]

    def descendants(iri: str) -> list[str]:
        out: list[str] = []
        stack = list(children.get(iri, []))
        while stack:
            node = stack.pop()
            out.append(node)
            stack.extend(children.get(node, []))
        return out

    def depth_below(iri: str, root: str) -> int:
        depth = 0
        node = iri
        while node != root and depth < 20:
            parents = [p for p in classes[node]["parents"] if p in classes]
            if not parents:
                break
            node = parents[0]
            depth += 1
        return depth

    wiki_by_name = {_norm(p["name"]): p for p in wiki.values()}

    def wiki_for(label: str) -> dict | None:
        page = wiki_by_name.get(_norm(label))
        if page is None:
            return None
        return {
            "title": page["title"],
            "curation_status": page["curation_status"],
            "created": page["created"],
            "definition_differs": _norm(page["definition"]) != _norm(classes[by_label[label]]["definition"])
            if label in by_label
            else None,
        }

    def row(iri: str, root: str) -> dict:
        c = classes[iri]
        label = label_of(iri)
        parent = next((p for p in c["parents"] if p in classes), None)
        return {
            "id": c["id"],
            "iri": iri,
            "label": label,
            "label_source": "owl" if c["label"] else ("fma_lookup" if c["id"] in FMA_LABELS else "id"),
            "definition": c["definition"],
            "definition_sources": c["definition_sources"],
            "editor_notes": c["editor_notes"],
            "comments": c["comments"],
            "source": c["source"],
            "curation_status": c["curation_status"],
            "date": c["date"],
            "parent_id": short_id(parent) if parent else None,
            "parent_label": label_of(parent),
            "depth": depth_below(iri, root),
            "children": len(children.get(iri, [])),
            "wiki": wiki_for(label),
        }

    # Branches and their members.
    branch_rows = []
    members: dict[str, list[dict]] = {}
    for kind, label in BRANCHES:
        root = by_label.get(label)
        if root is None:
            raise SystemExit(f"OWL has no class labelled {label!r}; the file has changed shape.")
        found = descendants(root)
        members[kind] = sorted((row(iri, root) for iri in found), key=lambda r: (r["depth"], r["label"].lower()))
        branch_rows.append(
            {
                "kind": kind,
                "id": short_id(root),
                "label": label,
                "definition": classes[root]["definition"],
                "direct_children": len(children.get(root, [])),
                "descendants": len(found),
            }
        )

    # Explicit stimuli carry their modality as an allValuesFrom restriction on
    # has_stimulus_modality; attach it to the row.
    modality_of: dict[str, list[str]] = {}
    blank_fillers = []
    for r in owl["restrictions"]:
        if r["fillers"]:
            modality_of[r["class"]] = [label_of(f) for f in r["fillers"]]
        else:
            blank_fillers.append(label_of(r["class"]))
    for r in members["explicit_stimulus"]:
        r["stimulus_modality"] = modality_of.get(r["iri"], [])

    # Wiki values per dimension, and what each side has that the other lacks.
    dimensions = {}
    for kind in DIMENSIONS:
        owl_names = {_norm(r["label"]): r["label"] for r in members[kind]}
        wiki_pages = [p for p in wiki.values() if p["is_term"] and _norm(p["parent"]) == _norm(WIKI_PARENTS[kind])]
        wiki_names = {_norm(p["name"]): p["name"] for p in wiki_pages}
        dimensions[kind] = {
            "root_id": next(b["id"] for b in branch_rows if b["kind"] == kind),
            "root_label": next(b["label"] for b in branch_rows if b["kind"] == kind),
            "owl_values": len(members[kind]),
            "wiki_values": len(wiki_pages),
            "values": members[kind],
            "wiki_only": [
                {
                    "title": p["title"],
                    "label": p["name"],
                    "definition": p["definition"],
                    "definition_source": p["definition_source"],
                    "curation_status": p["curation_status"],
                    "created": p["created"],
                }
                for p in sorted(wiki_pages, key=lambda p: p["name"].lower())
                if _norm(p["name"]) not in owl_names
            ],
            "owl_only": sorted(label for key, label in owl_names.items() if key not in wiki_names),
        }

    # Paradigms against the wiki.
    paradigm_names = {_norm(r["label"]) for r in members["paradigm"]}
    wiki_paradigms = [
        p
        for p in wiki.values()
        if p["is_term"]
        and p["title"] != "Behavioral_Experimental_Paradigm"
        and (_norm(p["parent"]) == "behavioral experimental paradigm" or p["title"].endswith("_Paradigm"))
    ]
    wiki_only_paradigms = [
        {
            "title": p["title"],
            "label": p["name"],
            "parent": p["parent"],
            "definition": p["definition"],
            "curation_status": p["curation_status"],
            "created": p["created"],
        }
        for p in sorted(wiki_paradigms, key=lambda p: p["name"].lower())
        if _norm(p["name"]) not in paradigm_names
    ]
    wiki_paradigm_names = {_norm(p["name"]) for p in wiki_paradigms}
    owl_only_paradigms = sorted(r["label"] for r in members["paradigm"] if _norm(r["label"]) not in wiki_paradigm_names)

    # Curation state on both sides.
    statuses = collections.Counter(c["curation_status"] or "(none)" for c in classes.values())
    years = collections.Counter(_year(c["date"]) for c in classes.values())
    wiki_statuses = collections.Counter(p["curation_status"].lower() or "(none)" for p in wiki.values() if p["is_term"])
    wiki_years = collections.Counter(_year(p["created"]) for p in wiki.values() if p["is_term"])

    # Hygiene.
    cogpo_ns = [c for c in classes.values() if "cogpo.org" in c["iri"]]
    name_iris = sorted(c["label"] for c in cogpo_ns if not c["id"].startswith("COGPO_"))
    label_iri_mismatch = [
        {"iri_name": c["id"], "label": c["label"]}
        for c in sorted(cogpo_ns, key=lambda c: c["id"])
        if not c["id"].startswith("COGPO_") and _norm(c["id"]) != _norm(c["label"])
    ]
    hygiene = {
        "unlabeled_classes": sorted(c["id"] for c in classes.values() if not c["label"]),
        "labeled_without_definition": sorted(c["label"] for c in classes.values() if c["label"] and not c["definition"]),
        "csv_quoted_definitions": sum(1 for c in classes.values() if c["definition_csv_quoted"]),
        "name_based_iris": len(name_iris),
        "name_based_iri_labels": name_iris,
        "label_iri_mismatch": label_iri_mismatch,
        "restrictions_with_blank_filler": sorted(blank_fillers),
        "wiki_definitions_with_external_links": [
            {"title": p["title"], "links": p["definition_external_links"]}
            for p in sorted(wiki.values(), key=lambda p: p["title"])
            if p["definition_external_links"]
        ],
        "wiki_definitions_differing_from_owl": sorted(
            r["label"] for kind in members for r in members[kind] if r["wiki"] and r["wiki"]["definition_differs"]
        ),
    }

    external = collections.Counter()
    for c in classes.values():
        if "cogpo.org" in c["iri"]:
            external["cogpo"] += 1
        elif "FMA" in c["iri"]:
            external["fma"] += 1
        elif "ifomis.org/bfo" in c["iri"]:
            external["bfo"] += 1
        elif "obolibrary" in c["iri"]:
            external["obo"] += 1
        else:
            external["other"] += 1

    return {
        "archive_name": archive.name,
        "harvested_on": manifest.get("started_on", ""),
        "source": {
            "owl_url": owl_entry.get("url", ""),
            "owl_bytes": owl_entry.get("bytes"),
            "owl_sha256": owl_entry.get("sha256", ""),
            "owl_identical_to": owl_entry.get("identical_to", []),
            "imports": owl["imports"],
            "imports_not_archived": manifest.get("imports_not_archived", []),
            "wiki_url": manifest.get("source", {}).get("wiki", ""),
            "wiki_pages_archived": len(wiki),
        },
        "inventory": {
            "classes": len(classes),
            "classes_labeled": sum(1 for c in classes.values() if c["label"]),
            "classes_defined": sum(1 for c in classes.values() if c["definition"]),
            "classes_by_namespace": dict(external.most_common()),
            "classes_with_cogpo_id": sum(1 for c in classes.values() if c["id"].startswith("COGPO_")),
            "object_properties": len(owl["properties"]),
            "annotation_properties": owl["annotation_properties"],
            "restrictions": len(owl["restrictions"]),
            "disjointness_axioms": owl["disjoint_axioms"],
            "individuals": len(owl["individuals"]),
            "paradigms": len(members["paradigm"]),
            "paradigms_direct": next(b["direct_children"] for b in branch_rows if b["kind"] == "paradigm"),
            "wiki_pages": len(wiki),
            "wiki_term_pages": sum(1 for p in wiki.values() if p["is_term"]),
            "wiki_paradigm_pages": len(wiki_paradigms),
        },
        "branches": branch_rows,
        "paradigms": members["paradigm"],
        "conditions": members["condition"],
        "dimensions": dimensions,
        "paradigm_comparison": {
            "owl_paradigms": len(members["paradigm"]),
            "wiki_paradigms": len(wiki_paradigms),
            "wiki_only": wiki_only_paradigms,
            "owl_only": owl_only_paradigms,
        },
        "object_properties": [
            {
                "id": p["id"],
                "label": p["label"] or p["id"],
                "domain": label_of(p["domain"]),
                "range": label_of(p["range"]),
                "parent": short_id(p["parent"]) if p["parent"] else None,
            }
            for p in owl["properties"]
        ],
        "individuals": owl["individuals"],
        "curation": {
            "owl_status": [{"label": k, "count": v} for k, v in statuses.most_common()],
            "owl_years": [{"year": k, "count": v} for k, v in sorted(years.items())],
            "wiki_status": [{"label": k, "count": v} for k, v in wiki_statuses.most_common()],
            "wiki_years": [{"year": k, "count": v} for k, v in sorted(wiki_years.items())],
        },
        "hygiene": hygiene,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).parent.parent / "data" / "cogpo_summary.json",
    )
    args = parser.parse_args()

    if not args.archive.exists():
        raise SystemExit(f"Archive not found: {args.archive}. Run src/fetch_cogpo_data.py first.")

    summary = build(args.archive)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(summary, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    inv = summary["inventory"]
    print(
        f"Wrote {args.out} ({inv['classes']} classes, {inv['paradigms']} paradigms, {inv['wiki_term_pages']} wiki term pages)."
    )


if __name__ == "__main__":
    main()
