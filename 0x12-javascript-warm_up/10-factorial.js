#!/usr/bin/node
function factorial (arg) {
  if (isNaN(arg)) {
    return (1);
  } else if (arg === 0 || arg === 1) {
    return (1);
  } else {
    return (arg * factorial(arg - 1));
  }
}
const arg = parseInt(process.argv[2]);
const result = factorial(arg);
console.log(result);
