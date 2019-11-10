class Solution {
    public void moveZeroes(int[] nums) {
        
        int zeroCount = 0;
        int i = 0;
        
        while (i<nums.length) {
            if (nums[i] == 0) {
                zeroCount++;
            } else if (zeroCount > 0) {
                nums[i-zeroCount] = nums[i];
                nums[i] = 0;
            }
            i++;
        }
    }
}