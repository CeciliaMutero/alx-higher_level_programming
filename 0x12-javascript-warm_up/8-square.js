#!/usr/bin/node
const i = parseInt(process.argv[2]);
if (isNaN(i)) {
  console.log('Missing size');
} else {
  if (i > 0) {
    for (let y = 0; y < i; y++) {
      console.log('x'.repeat(i));
    }
  }
}
