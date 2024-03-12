#!/usr/bin/node
exports.converter = function (base) {
  // Use the arguments object to access the provided number
  const number = arguments[1];

  // Use the toString method to convert the number to the specified base
  const result = number.toString(base);

  // Print the result
  console.log(result);
};

// Example usage:
// Replace '2' with the desired base and '10' with the number you want to convert
exports.converter(2, 10);
