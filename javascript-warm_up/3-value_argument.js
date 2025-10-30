#!/usr/bin/node
const arg = process.argv[2];
if (arg === undefined || arg === null || arg === '' || arg === 0 || arg === false) {
  console.log('No argument');
} else {
  console.log(arg);
}
