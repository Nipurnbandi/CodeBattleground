const fs = require('fs');

const values = fs.readFileSync(0, 'utf8').trim().split(/\s+/).map(Number);
const n = values[0];
const nums = values.slice(1, n + 1);
const target = values[n + 1];
const seen = new Map();

for (let index = 0; index < nums.length; index += 1) {
  const complement = target - nums[index];
  if (seen.has(complement)) {
    console.log(`${seen.get(complement)} ${index}`);
    break;
  }
  seen.set(nums[index], index);
}