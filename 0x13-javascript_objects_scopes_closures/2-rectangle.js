#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }
  toString() {
    if (!this.width || !this.height) {
      return "Rectangle {}";
    } else {
      return `Rectangle { width: ${this.width}, height: ${this.height} }`;
    }
  }
}
module.exports = Rectangle;
