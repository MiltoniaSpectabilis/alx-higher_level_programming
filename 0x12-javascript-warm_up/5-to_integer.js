#!/usr/bin/node
//
const argStr = process.argv[2];
const argNum = Number(argStr);

if (Number.isInteger(argNum)) {
  console.log(`My number: ${argNum}`);
} else {
  console.log('Not a number');
}
