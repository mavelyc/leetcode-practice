class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        
        hi, lo = len(S), 0
        final = []
        
        for ch in S:
            if ch == "I":
                final.append(lo)
                lo+=1
            else:
                final.append(hi)
                hi-=1
        
        return final + [lo]
