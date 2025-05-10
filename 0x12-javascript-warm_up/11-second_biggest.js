#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
if (args.length < 2) {
  console.log(0);
  process.exit(0);
}
const max = Math.max(...args);
const filtered = args.filter(n => n !== max);
console.log(Math.max(...filtered));
