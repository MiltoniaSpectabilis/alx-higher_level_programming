#!/usr/bin/node

const file = process.argv[2];
try {
  const fs = require('fs');
  const data = fs.readFileSync(file, 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
