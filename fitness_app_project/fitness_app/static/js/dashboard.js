$(".create").on("click", function(e) {
  e.preventDefault();
  $("#createMeal").on("click", function() {
    $("#mealCreate").css("display", "block")
  })
  $("#createCircuit").on("click", function() {
    $("#circuitCreate").css("display", "block");
  })
})
