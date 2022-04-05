#!/usr/bin/node

const process = require('process');

const n = parseInt(process.argv[2]);

function getFactorial (n) {
  if (n === 1) {
    return (1);
  }
  return (n * getFactorial(n - 1));
}

if (isNaN(n)) {
  console.log('1');
} else {
  console.log(getFactorial(n));
}
