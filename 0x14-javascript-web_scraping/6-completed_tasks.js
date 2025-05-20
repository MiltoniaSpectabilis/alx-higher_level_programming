#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) return;
  const data = JSON.parse(body);
  const obj = {};
  for (const i of data) {
    if (i.completed === true) {
      if (!obj[i.userId]) {
        obj[i.userId] = 1;
      } else {
        obj[i.userId] += 1;
      }
    }
  }
  console.log(obj);
});
