#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  if (size > 0) {
    for (let y = 0; y < size; y++) {
      let output = '';
      for (let i = 0; i < size; i++) {
        output += 'X';
      }
       console.log(output);
    }
  }
}
