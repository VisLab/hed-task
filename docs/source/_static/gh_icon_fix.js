/* Turn Furo's "view source on GitHub" header icon into a link to the repository root,
   and hide the "edit this page" icon. The pages under docs/ are generated, so a link to
   the source of one page is not useful; the repository is. Styling of the hijacked link
   is in custom.css under .github-repo-link. */
document.addEventListener("DOMContentLoaded", function () {
    const REPO_URL = "https://github.com/hed-standard/hed-task";

    document.querySelectorAll(".content-icon-container a").forEach(function (link) {
        const href = link.getAttribute("href");
        if (!href || !href.includes("github.com")) {
            return;
        }
        if (href.includes("/edit/")) {
            link.style.display = "none";
            link.classList.add("hidden-edit-link");
        } else if (href.includes("/blob/") || href.includes("/tree/")) {
            link.href = REPO_URL;
            link.title = "Go to the hed-task repository";
            link.setAttribute("aria-label", "Go to the hed-task repository");
            link.classList.add("github-repo-link");
            link.style.display = "inline-flex";
        }
    });
});
