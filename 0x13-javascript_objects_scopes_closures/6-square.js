#!/usr/bin/node
/**
 * class Square that inherits from previous class Square
 */
const prevSquare = require('./5-square');

class Square extends prevSquare {
  charPrint (c) {
    let swp = c;
    let myVar = '';
    if (c === undefined) {
      swp = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      myVar += swp;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(myVar);
    }
  }
}
module.exports = Square;
