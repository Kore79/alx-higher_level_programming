#!/usr/bin/node
const dict = require('./101-data').dict;

// Create a new dictionary where keys are numbers of occurrences and values are lists of user ids
const occurrencesDict = {};

// Iterate over the original dictionary
for (const userId in dict) {
  const occurrences = dict[userId];

  // If occurrences is not a key in the new dictionary, create an empty array
  occurrencesDict[occurrences] = occurrencesDict[occurrences] || [];

  // Add the current userId to the list of user ids for the corresponding occurrences
  occurrencesDict[occurrences].push(userId);
}

// Print the new dictionary
console.log(occurrencesDict);

