// Wait for the DOM to be fully loaded
$(document).ready(function () {
  // URL of the API
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  // Fetch data from the API
  $.get(url, function (data) {
    // Extract the results (array of movies) from the response data
    const movies = data.results;

    // Iterate over each movie and add its title to the list
    $.each(movies, function (index, movie) {
      $('#list_movies').append($('<li>').text(movie.title));
    });
  });
});
