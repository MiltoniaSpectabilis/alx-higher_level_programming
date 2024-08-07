// Wait for the DOM to be fully loaded
$(document).ready(function () {
  // Add click event listener to the element with id 'red_header'
  $('#red_header').click(function () {
    // Add the 'red' class to the header element
    $('header').addClass('red');
  });
});
