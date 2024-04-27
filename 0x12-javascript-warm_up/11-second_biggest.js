#!/usr/bin/node
let max = Number.NEGATIVE_INFINITY;
let secmax = Number.NEGATIVE_INFINITY;
const args = process.argv.slice(2).map(Number);
if (args.length <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < args.length; i++) {
    if (args[i] > max) {
      secmax = max;
      max = args[i];
    }
  }
  console.log(secmax);
}
