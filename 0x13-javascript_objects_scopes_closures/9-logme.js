#!/usr/bin/node

exports.logMe = function (item) {
  const env = require('process');
  
  console.log(logList.length + ': ' + item);

  logList.push(item);
};
