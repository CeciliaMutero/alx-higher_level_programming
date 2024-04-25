#!/usr/bin/node
let i = 0;
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} while (i < parseInt(process.argv[2])) {
  console.log('C is fun');
  i++;
}
