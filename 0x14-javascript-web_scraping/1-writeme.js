#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const strToWrite = process.argv[3];
try {
  fs.writeFileSync(file, strToWrite, 'utf8');
} catch (err) {
  console.error(err);
}
