n = int(input())
nums = list(map(int, input().split()))
target = int(input())

seen = {}
for index, number in enumerate(nums[:n]):
    complement = target - number
    if complement in seen:
        print(seen[complement], index)
        break
    seen[number] = index