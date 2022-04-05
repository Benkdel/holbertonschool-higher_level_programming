#!/usr/bin/node

exports.nbOccurences = function (list = [], searchElemtn) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElemtn) {
      count++;
    }
  }
  return (count);
};
