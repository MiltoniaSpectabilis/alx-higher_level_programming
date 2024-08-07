// Wait for the DOM to be fully loaded
$(document).ready(function () {
  // Add click event listener to the element with id 'toggle_header'
  $('#toggle_header').click(function () {
    // Toggle between 'red' and 'green' classes on the header element
    $('header').toggleClass('red green');
  });
});
