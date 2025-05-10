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
      process.stdout.write(c.repeat(this.size) + '\n');
    }
  }
}

module.exports = Square;
