// Wrap the code in a function that runs when the DOM is fully loaded
$(function () {
  // URL of the API
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Fetch data from the API
  $.get(url, function (data) {
    // Extract the 'hello' value from the response data
    const helloTranslation = data.hello;

    // Display the translation in the div with id 'hello'
    $('#hello').text(helloTranslation);
  });
});
