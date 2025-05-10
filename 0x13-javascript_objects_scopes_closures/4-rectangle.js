#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (
      Number.isInteger(w) &&
      Number.isInteger(h) &&
      w > 0 &&
      h > 0
    ) {
      this.width = w;
      this.height = h;
    }
  }

  rotate () {
    let temp = null;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
}

module.exports = Rectangle;
