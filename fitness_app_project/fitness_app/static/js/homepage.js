const app_id = "&app_id=2d7d9644";
const app_key = "&app_key=8e911eeff3b68f04eafd1fffeaf16401";
// let food_params = '?ingr=' +

// In the request header
const wger_api_key = "3a799cb0dc24aa6c28713c85eb3f2be4eb6f48f0";
// Authorization: Token 3a799cb0dc24aa6c28713c85eb3f2be4eb6f48f0

const food_url_base = "https://api.edamam.com/api/food-database/parser";

// sample url if a user searched for 'red apple'. the '%20' represents a space.
// 'https://api.edamam.com/api/food-database/parser?ingr=red%20apple&app_id={your app_id}&app_key={your app_key}'
// this copy and paste the below URL into Postman if you want to have a look at the responses.
// 'https://api.edamam.com/api/food-database/parser?ingr=red%20apple&app_id=2d7d9644&app_key=8e911eeff3b68f04eafd1fffeaf16401'

// muscle endpoint
// exercise category
const error = (err1, err2, err3) => {
  console.log(err1);
  console.log(err2);
  console.log(err3);
};

const renderFoodSuccess = response => {
  $("#search_results").append(`
            <ul>
            <li>Food: ${response.hints.food.label}</li>
            <li>Calories: ${response.hints.food.nutrients.kcal}</li>
            <li>Protein: ${response.hints.food.nutrients.protein}</li>
            <li>Fat: ${response.hints.food.nutrients.fat}</li>
            <li>Carbs: ${response.hints.food.nutrients.carbs}</li>
            </ul>
            `);
};

const renderWorkoutSuccess = response => {
  $("#search_results").append(`
          <ul>
            <li>Author: ${response.license_author}</li>
            <li>Name: ${response.name}</li>
            <li>Description: ${resonse.description}</li>
          </ul>
    `);
};

// ####################################### AJAX CALLS ############################################

$("input[type='submit']").on("click", function(e) {
  e.preventDefault();
  if ($(".form-control").val() === "food") {
    // let food = $("input[name='search']").val();
    $.ajax({
      type: "GET",
      url: "/api/food/find",
      // data: "food":"food",
      success: renderFoodSuccess,
      error: error
    });
  } else if ($(".form-control").val() === "workouts") {
    // let workout = $("input[name='search']").val();
    $.ajax({
      type: "GET",
      url: "/api/workout/find",
      // data: "workout":"workout",
      success: renderWorkoutSuccess,
      error: error
    });
  }
});

const test = () => {
  console.log("invoked");
  $.ajax({
    type: "GET",
    url: "/api/workout/find",
    data:,
    success: response => {
      console.log(response);
      $("#search-results").append(`<p>${response}</p>`);
    },
    error: error
  });
};
