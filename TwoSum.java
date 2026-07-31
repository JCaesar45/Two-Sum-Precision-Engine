import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;

public class TwoSum {
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }
        return null;
    }

    public static void main(String[] args) {
        int[][] testCases = {
            {}, {7}, {1,3,5,7}, {-4,-1,0,3,5}, {3,2,3}, {1,4,2,3,5}, {0,0,0}
        };
        int[] targets = {9,14,20,-1,6,6,0};

        for (int t = 0; t < testCases.length; t++) {
            int[] result = twoSum(testCases[t], targets[t]);
            System.out.println("Test " + (t+1) + ": " + Arrays.toString(result));
        }
    }
}
