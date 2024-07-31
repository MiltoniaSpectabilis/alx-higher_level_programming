#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) return console.error(err);
  const todos = JSON.parse(body);
  const result = todos.reduce((acc, todo) => {
    if (todo.completed) {
      acc[todo.userId] = (acc[todo.userId] || 0) + 1;
    }
    return acc;
  }, {});

  console.log(result);
});
