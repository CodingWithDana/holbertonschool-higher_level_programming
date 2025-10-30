#!/usr/bin/node
const arg = process.arg[2];
if (arg == '') {
  console.log('No argument');
} else {
  console.log(arg);
}
