#!/usr/bin/node

const process = require('process');

const n1 = parseInt(process.argv[2]);
const n2 = parseInt(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(n1, n2);
