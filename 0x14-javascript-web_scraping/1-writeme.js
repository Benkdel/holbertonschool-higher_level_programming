#!/usr/bin/node

const fs = require('fs');
const process = require('process');

const filePath = process.argv[2];
const stringData = process.argv[3];

fs.writeFile(filePath, stringData, err => {
  if (err) {
    console.log(err);
  }
});
