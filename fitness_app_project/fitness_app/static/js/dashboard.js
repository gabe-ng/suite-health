$("#createMeal, #createCircuit").hover(
  function() {
    $(this).css("background-color", "#2cdad9");
    $(this)
      .children()
      .css("color", "#02243e");
  },
  function() {
    $(this).css("background-color", "#02243e");
    $(this)
      .children()
      .css("color", "#2cdad9");
  }
);
