{{USER_CODE}}

def main():
    count = int(input())
    nums = list(map(int, input().split()))
    target = int(input())

    answer = two_sum(nums, target)
    print(*answer)


if __name__ == "__main__":
    main()