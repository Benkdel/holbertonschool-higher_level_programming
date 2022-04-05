#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w * h > 0 && w > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
