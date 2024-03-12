#!/usr/bin/node
const list = require('./100-data').list;

// Use the map method to create a new array with values multiplied by their index
const newList = list.map((value, index) => value * index);

// Print the initial list and the new list
console.log('Initial List:', list);
console.log('New List:', newList);

