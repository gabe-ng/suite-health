// Chatbot
$(".chatbot-icon").on("click", function() {
  console.log("clicked");
  $(".chat").toggleClass("hide");
});

let workoutResponse = null;

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

//////////////////// Handle Errors //////////////////
const error = (err1, err2, err3) => {
  console.log(err1);
  console.log(err2);
  console.log(err3);
};

///////////////// Render Food and Workout Searches ///////////////
const renderFoodSuccess = response => {
  console.log(response);
  $("#search-results").empty();
  response.hints.forEach(food => {
    $("#search-results").append(`
        <div>
            <h1>Name: ${food.food.label}</h1>
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
  workoutResponse = response;
  $("#search-results").empty();
  response.results.forEach(workout => {
    // console.log(workout.id);
    $("#search-results").append(`
          <div id="${workout.id} class="rendered-workouts">
            <h1>Author: ${workout.license_author}</h1>
            <p>Name: ${workout.name}</p>
            <p>Description: ${workout.description}</p>
            <ul id="muscle-group-${workout.id}"></ul>
          </div>
    `);
    workout.muscles.forEach(muscleNum => {
      $(`#muscle-group-${workout.id}`).append(`<li>${muscles[muscleNum]}</li>`);
    });
    $("#search-results").append(
      `<input value='Save this workout' type='submit' class='saveWorkout' id=${
        workout.id
      } data-id='${workout.id}'>`
    );
  });
};

$("#find-button").on("click", function(e) {
  e.preventDefault();
  if ($("#search-type").val() === "food") {
    let foodInput = $("#food-selection").val();
    let food = foodInput.replace(/" "/g, "%20");
    console.log(food);
    $.ajax({
      method: "GET",
      url: "/api/food/find/" + food,
      success: renderFoodSuccess,
      error: error
    });
  } else if ($(".form-control").val() === "workouts") {
    let muscle = $("#muscle-selection").val();
    console.log("invoked");
    $.ajax({
      method: "GET",
      url: "/api/workout/find/" + muscle,
      success: renderWorkoutSuccess,
      error: error
    });
  }
});

/////////////////////// Save workouts and meals ////////////////////
$("#search-results").on("click", ".saveWorkout", function() {
  console.log("in search");
  // if workout id matches the input button id, save that work
  let workoutId = null;
  let license_author = null;
  let name = null;
  let description = null;
  let muscles = "muscles";

  workoutResponse.results.forEach(workout => {
    if (workout.id === $(this).data("id")) {
      console.log(workout);
      workoutId = workout.id;
      license_author = workout.license_author;
      name = workout.name;
      description = workout.description;
    }
  });

  $.ajax({
    type: "POST",
    url: "/api/workout/save/bjimison/",
    data: {
      workoutId: workoutId,
      author: license_author,
      name: name,
      description: description,
      muscles: "muscles"
    },
    dataType: "application/json",
    success: console.log("success")
  });
});

/////////////////////// Render Custom Meals and Circuits to Feed /////////
const renderCustomMeals = response => {
  let meals = JSON.parse(response.meals);
  console.log(meals);
  for (let i = 0; i < meals.length; i++) {
    let meal = meals[i];
    $("#meal-feed").append(`<div id="${meal.pk}">
                  <h6>Name: ${meal.fields.label}</h6>
                  <p>Ingredients: ${meal.fields.ingredients}</p>
                  <p>Instructions: ${meal.fields.instructions}</p>
                  <p>Portions: ${meal.fields.portions}</p>
                  <p>Macros: ${meal.fields.macros}</p>
                    </div>`);
  }
};

const renderCustomCircuits = response => {
  let circuits = JSON.parse(response.circuits);
  console.log(circuits);
  for (let i = 0; i < circuits.length; i++) {
    let circuit = circuits[i];
    $("#circuit-feed").append(`<div id="${circuit.pk}">
                  <h6>Name: ${circuit.fields.name}</h6>
                  <p>Workouts: ${circuit.fields.workouts}</p>
                    </div>`);
  }
};

$.ajax({
  method: "GET",
  url: "/api/custommeals/",
  success: renderCustomMeals,
  error: error
});

$.ajax({
  method: "GET",
  url: "/api/customcircuits/",
  success: renderCustomCircuits,
  error: error
});

///////////////////////////// /////////////////////
