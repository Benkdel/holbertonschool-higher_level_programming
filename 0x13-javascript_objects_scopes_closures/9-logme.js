#!/usr/bin/node

exports.logMe = function (item) {
  const { env } = require('process');
  env.Printed = !env.Printed ? 0 : parseInt(env.Printed) + 1;
  console.log(`${process.env.Printed}: ${item}`);
};
