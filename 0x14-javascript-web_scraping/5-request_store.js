#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) return;
  fs.writeFileSync(file, body, 'utf8');
});
