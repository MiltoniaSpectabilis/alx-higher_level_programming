#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occCounter = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      occCounter += 1;
    }
  }
  return occCounter;
};
