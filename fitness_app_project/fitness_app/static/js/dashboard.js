$("#createMeal, #createCircuit").css("background-color", "#02243e");

$("#createMeal, #createCircuit").hover(
  function() {
    $(this).css({ "background-color": "#2cdad9", color: "#02243e" });
  },
  function() {
    $(this).css({ "background-color": "#02243e", color: "#2cdad9" });
  }
);
