function largest_element(nums) {
  let largest = nums[0];
  for (const number of nums.slice(1)) {
    if (number > largest) {
      largest = number;
    }
  }
  return largest;
}

module.exports = { largest_element };
