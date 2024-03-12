#!/usr/bin/node
exports.esrever = function (list) {
  // Create a new array to store the reversed elements
  const reversedList = [];

  // Iterate over the original list in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  return reversedList;
};
