#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    /* reversedList[reversedList.length] = list[i];
    the above does the same thing as push().
    another alternative i found is to use a normal loop
    with unshift() */
    reversedList.push(list[i]);
  }
  return reversedList;
};
