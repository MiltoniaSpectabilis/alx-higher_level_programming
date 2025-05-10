#!/usr/bin/node

const list = require('./100-data').list;
console.log(list);
const multiplyByIdx = list.map((n, i) => n * i); /* takes both the element and the index */
console.log(multiplyByIdx);
