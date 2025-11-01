#!/usr/bin/node
const arg = process.argv.slice(2);
const intArg = arg.map(Number);

if (arg.length <= 1) {
  console.log(0);
  process.exit(0);
}

let max = intArg[0];
let secondMax = intArg[1];

if (secondMax > max) {
  [max, secondMax] = [secondMax, max];
}

for (let i = 2; i < intArg.length; i++) {
  if (intArg[i] > max) {
    secondMax = max;
    max = intArg[i];
  }
  if (intArg[i] < max && intArg[i] > secondMax) {
    secondMax = intArg[i];
  }
}
console.log(secondMax);
