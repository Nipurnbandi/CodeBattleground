const fs = require('fs');

const values = fs.readFileSync(0, 'utf8').trim().split(/\s+/).map(Number);
const n = values[0];
const nums = values.slice(1, n + 1);

let largest = nums[0];
for (const number of nums.slice(1)) {
  if (number > largest) {
    largest = number;
  }
}

console.log(largest);
