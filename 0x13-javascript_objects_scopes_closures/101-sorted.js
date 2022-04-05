#!/usr/bin/node

const dict1 = require('./101-data').dict;

const newDict = {};

console.log(dict1);

for (const k in dict1) {
  const keyExists = dict1[k] in newDict;

  if (keyExists) {
    newDict[dict1[k]].push(k);
  } else {
    const arrTemp = [];
    arrTemp.push(k);
    newDict[dict1[k]] = arrTemp;
  }
}

console.log(newDict);
