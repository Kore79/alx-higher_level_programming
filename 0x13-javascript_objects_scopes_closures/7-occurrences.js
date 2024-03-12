#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // Use reduce to count occurrences of searchElement in the list
  const occurrences = list.reduce((count, element) => (element === searchElement ? count + 1 : count), 0);
  return occurrences;
};
