import java.util.*;
class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer,Integer> table = new HashMap<Integer,Integer>();
        for(int num: arr){
            if (table.containsKey(num)){
                table.put(num, table.get(num) + 1);
            } else {
                table.put(num, 1);
            }
        }
        Set<Integer> setKeys = new HashSet<Integer>(table.values());
        
        return (setKeys.size() == table.keySet().size());
    }
}