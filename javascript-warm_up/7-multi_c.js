#!/usr/bin/node
const firstArgument = process.argv[2];
const toPrint = 'C is fun';
if (isNaN(firstArgument)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstArgument; i++) {
    console.log(toPrint);
  }
}
