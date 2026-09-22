/* Keep pop-up cards (.pop-card, see custom.css) inside the content column.

   A card opens below its trigger, aligned to the trigger's left edge. When the trigger
   sits near the right edge of the column, the card would run past it and be clipped by
   the column's overflow, so on open the card is measured and, if it would overflow,
   flipped to align with the trigger's right edge instead (class pop-flip). Cards are
   emitted by src/generators/task_pages.py. */
document.addEventListener("DOMContentLoaded", function () {
  var content = document.querySelector(".content") || document.body;

  function place(pop) {
    var card = pop.querySelector(".pop-card");
    if (!card) {
      return;
    }
    pop.classList.remove("pop-flip");
    var bounds = content.getBoundingClientRect();
    var rect = card.getBoundingClientRect();
    if (rect.right > bounds.right - 8 && rect.width < bounds.width) {
      pop.classList.add("pop-flip");
    }
  }

  document.querySelectorAll(".pop").forEach(function (pop) {
    pop.addEventListener("mouseenter", function () {
      place(pop);
    });
    pop.addEventListener("focusin", function () {
      place(pop);
    });
  });
});
