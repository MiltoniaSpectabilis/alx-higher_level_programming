// Wait for the DOM to be fully loaded
$(document).ready(function () {
  // Add click event listener to the element with id 'red_header'
  $('#red_header').click(function () {
    // Change the text color of the header to red
    $('header').css('color', '#FF0000');
  });
});
