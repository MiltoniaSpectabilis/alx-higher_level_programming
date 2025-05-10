#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);
const firstFile = args[0];
const secondFile = args[1];
const thirdFile = args[2];

let contentToWrite = '';

fs.readFile(firstFile, 'utf8', (err, data) => {
  if (err) throw err;
  contentToWrite = data;

  fs.readFile(secondFile, 'utf8', (err, data) => {
    if (err) throw err;
    contentToWrite += data;

    fs.writeFile(thirdFile, contentToWrite, () => {
    });
  });
});
