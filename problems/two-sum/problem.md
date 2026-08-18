# Two Sum

You are given an array of integers `nums` and an integer `target`.

Return the **zero-based indices** of two different elements whose sum equals
`target`.

You may assume that exactly one valid answer exists.

## Input format

- The first line contains an integer `n`, the number of elements.
- The second line contains `n` space-separated integers.
- The third line contains the integer `target`.

## Output format

Print two space-separated zero-based indices whose corresponding values add up
to `target`.

## Constraints

- `2 <= n <= 100000`
- `-1000000000 <= nums[i] <= 1000000000`
- `-1000000000 <= target <= 1000000000`
- Exactly one valid answer exists.

## Example

### Input

```text
4
2 7 11 15
9
```

### Output

```text
0 1
```

## Explanation

`nums[0] + nums[1] = 2 + 7 = 9`, so the answer is `0 1`.