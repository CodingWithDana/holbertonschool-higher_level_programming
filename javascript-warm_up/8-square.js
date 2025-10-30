#!/usr/bin/node
const sizeOfSquare = process.argv[2];
const toPrint = 'X';
if (isNaN(sizeOfSquare)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sizeOfSquare; i++) {
    let row = '';
    for (let j = 0; j < sizeOfSquare; j++) {
      row += toPrint;
    }
    console.log(row);
  }
}
