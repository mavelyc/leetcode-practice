class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = collections.defaultdict(int)
        
        for i in arr:
            dic[i]+=1
            
        return True if len(set(dic.values())) == len(dic) else False
