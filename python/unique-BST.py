class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        ref = [0 for _ in range(n+1)]
        ref[0] = ref[1] = 1
    
        if n < 2: return 1
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                ref[i] += ref[j-1]*ref[i-j]
                
        return ref[n]