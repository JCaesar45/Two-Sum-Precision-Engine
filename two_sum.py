def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None


def run_tests():
    tests = [
        ([], 9, None),
        ([7], 14, None),
        ([1, 3, 5, 7], 20, None),
        ([-4, -1, 0, 3, 5], -1, [0, 3]),
        ([3, 2, 3], 6, [0, 2]),
        ([1, 4, 2, 3, 5], 6, [1, 2]),
        ([2**31 - 2, 1, -2**31], 2**31 - 1, [0, 1]),
        ([0, 0, 0], 0, [0, 1]),
    ]

    for idx, (nums, target, expected) in enumerate(tests, 1):
        result = two_sum(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {idx}: {status} | nums={nums} target={target} → {result}")

if __name__ == "__main__":
    run_tests()
