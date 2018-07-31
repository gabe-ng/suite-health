let muscles = {
  1: "Biceps Long Head",
  2: "Deltiods",
  3: "Serratus Anterior",
  4: "Chest",
  5: "Triceps",
  6: "Abdominals",
  7: "Calves",
  8: "Glutes",
  9: "Traps",
  10: "Quadriceps",
  11: "Hamstring",
  12: "Lats",
  13: "Bicep Short Head",
  14: "Obliques",
  15: "Calves"
};

// muscle endpoint
// exercise category
const error = (err1, err2, err3) => {
  console.log(err1);
  console.log(err2);
  console.log(err3);
};

const renderFoodSuccess = response => {
  console.log(response);
  $("#search-results").empty();
  response.hints.forEach(food => {
    $("#search-results").append(`
        <div>
            <h6>Name: ${food.food.label}</h6>
            <ul id="${food.food.id}"></ul>
        </div>
    `);
    for (let nutrient in food.food.nutrients) {
      let measure = food.food.nutrients[nutrient];
      $(`#${food.food.id}`).append(`
            <li>${nutrient} : ${measure}</li>
        `);
    }
  });
};

const renderWorkoutSuccess = response => {
  $("#search-results").empty();
  response.results.forEach(workout => {
    console.log(workout.id);
    $("#search-results").append(`
          <div id="${workout.id} class="rendered-workouts">
            <h6>Author: ${workout.license_author}</h6>
            <p>Name: ${workout.name}</p>
            <p>Description: ${workout.description}</p>
            <ul id="muscle-group-${workout.id}"></ul>
          </div>
    `);
    workout.muscles.forEach(muscleNum => {
      $(`#muscle-group-${workout.id}`).append(`<li>${muscles[muscleNum]}</li>`);
    });
  });
};

// ####################################### AJAX CALLS ############################################

$("#find-button").on("click", function(e) {
  e.preventDefault();
  if ($("#search-type").val() === "food") {
    let foodInput = $("#food-selection").val();
    let food = foodInput.replace(/" "/g, "%20");
    console.log(food);
    $.ajax({
      type: "GET",
      url: "/api/food/find/" + food,
      success: renderFoodSuccess,
      error: error
    });
  } else if ($(".form-control").val() === "workouts") {
    let muscle = $("#muscle-selection").val();
    console.log("invoked");
    $.ajax({
      type: "GET",
      url: "/api/workout/find/" + muscle,
      success: renderWorkoutSuccess,
      error: error
    });
  }
});

const test = () => {
  let limit = $("input[name='search']").val();
  console.log("invoked");
  $.ajax({
    type: "GET",
    url: "/api/workout/find/" + limit,
    success: response => {
      console.log(response);
      $("#search-results").append(`<p>${response.results[0].id}</p>
      <p>${response.results[0].description}</p>`);
    },
    error: error
  });
};
