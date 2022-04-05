#!/usr/bin/node

exports.callMeMoby = function callMeMoby (x, func) {
  for (let i = 0; i < x; i++) {
    func();
  }
};
