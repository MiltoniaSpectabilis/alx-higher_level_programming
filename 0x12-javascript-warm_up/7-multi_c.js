#!/usr/bin/node

const strToPrint = 'C is fun';
const numberOfIterations = process.argv[2];

// check if the arg can be converted to an int
// it implicitly converts the arg to an int if true
if (!Number(numberOfIterations)) {
  console.log('Missing number of occurrences');
}

// print the str according to the arg.
for (let i = 0; i < numberOfIterations; i++) {
  console.log(strToPrint);
}
