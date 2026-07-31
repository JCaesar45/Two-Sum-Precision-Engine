function twoSum(nums: number[], target: number): number[] | null {
  const seen = new Map<number, number>();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (seen.has(complement)) {
      return [seen.get(complement)!, i];
    }
    seen.set(nums[i], i);
  }
  return null;
}

// Quick self-test
const tests: [number[], number, number[] | null][] = [
  [[], 9, null],
  [[7], 14, null],
  [[1, 3, 5, 7], 20, null],
  [[-4, -1, 0, 3, 5], -1, [0, 3]],
  [[3, 2, 3], 6, [0, 2]],
  [[1, 4, 2, 3, 5], 6, [1, 2]],
  [[0, 0, 0], 0, [0, 1]],
];

tests.forEach(([nums, target, expected], i) => {
  const result = twoSum(nums, target);
  const pass = JSON.stringify(result) === JSON.stringify(expected);
  console.log(`Test ${i + 1}: ${pass ? "PASS" : "FAIL"} → ${result}`);
});
