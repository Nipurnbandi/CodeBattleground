def largest_element(nums):
    largest = nums[0]
    for number in nums[1:]:
        if number > largest:
            largest = number
    return largest
