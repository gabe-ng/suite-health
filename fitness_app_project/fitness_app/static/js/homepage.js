const app_id = '&app_id=2d7d9644';
const app_key = '&app_key=8e911eeff3b68f04eafd1fffeaf16401';
let food_params = '?ingr=' + 

// In the request header
const wger_api_key = '3a799cb0dc24aa6c28713c85eb3f2be4eb6f48f0';
// Authorization: Token 3a799cb0dc24aa6c28713c85eb3f2be4eb6f48f0

const food_url_base = 'https://api.edamam.com/api/food-database/parser';


// food_view html rendering

$('#food_btn').on('click', () => {
    $.ajax({
        type: 'GET',
        url: {% views 'food_view' %},
        success: (response) => {
            $('#search-results').append(`
            <ul>
            <li>Food: ${response.hints.food.label}</li>
            <li>Calories: ${response.hints.food.nutrients.kcal}</li>
            <li>Protein: ${response.hints.food.nutrients.protein}</li>
            <li>Fat: ${response.hints.food.nutrients.fat}</li>
            <li>Carbs: ${response.hints.food.nutrients.carbs}</li>
            </ul>
            `);
        }
    });
});
