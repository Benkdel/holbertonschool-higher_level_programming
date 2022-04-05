#!/usr/bin/node

const dict1 = require('./101-data').dict;

let newDict = {};

console.log(dict1);

for (let k in dict1){
  let keyExists = dict1[k] in newDict;

  if (keyExists) {
    newDict[dict1[k]].push(k);
  } else {
    let arrTemp = [];
    arrTemp.push(k);
    newDict[dict1[k]] = arrTemp;
  }
}

console.log(newDict);
