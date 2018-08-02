// $(document).ready(function(){
//     $.ajax({
//     url: "http://exbook.herokuapp.com/api/users",
//     method: 'POST',
//     data: signData,
//     success: signSuccess,
//     error: mapError
//   });
//   $('#foodList')
// })
console.log("yo");
$("#mealList").on("click", "input[name='delete_items]'", function(e) {
  e.preventDefault();
  console.log("in delete mode");
  $(this)
    .parent()
    .remove();
});
