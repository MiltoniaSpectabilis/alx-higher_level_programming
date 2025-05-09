#!/usr/bin/node

const numOfIters = process.argv[2];

if (!Number(numOfIters)) {
  console.log('Missing size');
}

for (let i = 0; i < numOfIters; i++) {
  for (let j = 0; j < numOfIters; j++) {
    process.stdout.write('X');
  }
  process.stdout.write('\n');
}
