#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) return;
  const data = JSON.parse(body);
  const films = data.results;
  let counter = 0;
  for (let i = 0; i < films.length; i++) {
    const filmCharacters = films[i].characters;
    for (let j = 0; j < filmCharacters.length; j++) {
      if (films[i].characters[j].includes('/18/')) {
        counter += 1;
      }
    }
  }
  console.log(counter);
});
