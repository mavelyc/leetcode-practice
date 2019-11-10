import java.util.*;
class Solution {
    public int majorityElement(int[] nums) {
        int count = nums.length/2;
        int finalNum = 0;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for(int curr: nums){
            if (map.containsKey(curr)){
                map.put(curr, map.get(curr) + 1);
                if (map.get(curr) > count)
                    finalNum = curr;
            } else {
                map.put(curr, 1);
                if (map.get(curr) > count)
                    finalNum = curr;
            }
        }
        return finalNum;
    }
}