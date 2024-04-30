#!/usr/bin/node
const Square6 = require('./5-square');
class Square extends Square6 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let output = '';
      for (let y = 0; y < this.width; y++) {
        output += c;
      }
      console.log(output);
    }
  }
}
module.exports = Square;
