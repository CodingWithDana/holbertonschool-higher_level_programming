#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const firstInteger = parseInt(process.argv[2]);
const secondInteger = parseInt(process.argv[3]);

if (isNaN(firstInteger, secondInteger) || !firstInteger || !secondInteger) {
  console.log('NaN');
} else {
  const sum = add(firstInteger, secondInteger);
  console.log(sum);
}
