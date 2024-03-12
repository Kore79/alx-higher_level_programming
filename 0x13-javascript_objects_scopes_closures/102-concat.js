#!/usr/bin/node
const fs = require('fs');
const path = require('path');

// Ensure correct number of command line arguments
if (process.argv.length !== 5) {
  console.error('Usage: ./concatFiles.js <sourceFile1> <sourceFile2> <destinationFile>');
  process.exit(1);
}

// Get file paths from command line arguments
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

// Read the content of the first source file
fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${sourceFile1}:`, err);
    process.exit(1);
  }

  // Read the content of the second source file
  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${sourceFile2}:`, err);
      process.exit(1);
    }

    // Concatenate the contents of the two files
    const concatenatedData = data1 + data2;

    // Write the concatenated content to the destination file
    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${destinationFile}:`, err);
        process.exit(1);
      }

      console.log(`Files ${sourceFile1} and ${sourceFile2} concatenated to ${destinationFile}.`);
    });
  });
});

