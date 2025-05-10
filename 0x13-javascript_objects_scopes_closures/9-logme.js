#!/usr/bin/node

let argsPrintedCounter = 0;

exports.logMe = function logMe (item) {
  console.log(argsPrintedCounter + ': ' + item);
  argsPrintedCounter += 1;
};
