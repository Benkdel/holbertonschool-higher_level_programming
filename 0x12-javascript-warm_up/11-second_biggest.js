#!/usr/bin/node

const process = require('process');

const argv = process.argv;

const sortedArray = [];

for (let i = 2; i < argv.length; i++) {
  sortedArray.push(argv[i]);
}

sortedArray.sort((a, b) => b - a);

console.log(sortedArray[1]);
