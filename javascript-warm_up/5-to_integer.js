#!/usr/bin/node
const arg = process.argv[2];
// if arg is not a number OR arg is missing/empty
if (isNaN(arg) || !arg) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(arg)}`);
}
