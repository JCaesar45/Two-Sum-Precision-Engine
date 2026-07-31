def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None


# ---------- Test Cases ----------

def run_tests():
    tests = [
        # 1. Empty list
        ([], 9, None),

        # 2. Single element
        ([7], 14, None),

        # 3. No valid pair
        ([1, 3, 5, 7], 20, None),

        # 4. Negative numbers + zero
        ([-4, -1, 0, 3, 5], -1, [0, 3]),

        # 5. Duplicates that form the target
        ([3, 2, 3], 6, [0, 2]),

        # 6. Multiple valid pairs (first found is acceptable)
        ([1, 4, 2, 3, 5], 6, [1, 2]),   # 4 + 2

        # 7. Large integers
        ([2**31 - 2, 1, -2**31], 2**31 - 1, [0, 1]),

        # 8. All zeros, target zero
        ([0, 0, 0], 0, [0, 1]),
    ]

    for idx, (nums, target, expected) in enumerate(tests, 1):
        result = two_sum(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {idx}: {status}")
        print(f"  Input    : nums={nums}, target={target}")
        print(f"  Expected : {expected}")
        print(f"  Got      : {result}")
        print()

if __name__ == "__main__":
    run_tests()
