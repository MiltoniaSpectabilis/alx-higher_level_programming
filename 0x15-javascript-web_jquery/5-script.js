// Wait for the DOM to be fully loaded
$(document).ready(function () {
  // Add click event listener to the element with id 'add_item'
  $('#add_item').click(function () {
    // Create a new <li> element with the text 'Item'
    const newItem = $('<li>').text('Item');

    // Append the new <li> element to the <ul> with class 'my_list'
    $('ul.my_list').append(newItem);
  });
});
