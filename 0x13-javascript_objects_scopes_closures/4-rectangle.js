#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w * h > 0 && w > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }

  rotate () {
    const tempWidth = this.width;
    this.width = this.height;
    this.height = tempWidth;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
