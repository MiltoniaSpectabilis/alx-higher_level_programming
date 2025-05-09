#!/usr/bin/node

function factorial (n) {
  if (n <= 1 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}

const arg = process.argv[2];
const n = Number(arg);
console.log(factorial(n));
