class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> diffIndexMap = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int diff = target - num;

            if (diffIndexMap.containsKey(diff)) {
                return new int[] { diffIndexMap.get(diff), i };
            }

            diffIndexMap.put(num, i);
        }

        return new int[] {};
    }
}
