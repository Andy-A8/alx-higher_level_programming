#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (size) {
  let row = '';
  for (let i = 0; i < size; i++) {
    row += 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
