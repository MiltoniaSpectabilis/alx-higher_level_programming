// Wait for the DOM to be fully loaded
$(document).ready(function () {
  // URL of the API
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  // Fetch data from the API
  $.get(url, function (data) {
    // Extract the name from the response data
    const characterName = data.name;

    // Display the name in the div with id 'character'
    $('#character').text(characterName);
  });
});
