n = int(input())
nums = list(map(int, input().split()))

largest = nums[0]
for number in nums[1:n]:
    if number > largest:
        largest = number

print(largest)
