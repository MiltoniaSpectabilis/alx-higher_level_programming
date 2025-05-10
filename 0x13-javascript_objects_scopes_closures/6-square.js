#!/usr/bin/node

const SquareBase = require('./5-square');

class Square extends SquareBase {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }

  /* i'm commenting this out as a learning note:
  i spent about 20 mins trying
  to figure out why the output wasn't doubling ='( */
  double () {
    this.size *= 2;
  }
}

module.exports = Square;
