#!/usr/bin/node

const strToPrint = 'C is fun';

// check if the arg is provided
if (!process.argv[2]) {
  console.log('Missing number of occurrences');
}
// convert the str to an int
const numberOfIterations = Number(process.argv[2]);

// print the str according to the arg
for (let i = 0; i < numberOfIterations; i++) {
  console.log(strToPrint);
}
