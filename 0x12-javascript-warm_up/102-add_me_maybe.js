#!/usr/bin/node

exports.addMeMaybe = function addMeMaybe (nb, func) {
  nb = nb + 1;
  func(nb);
};
