def climbStairs(self, n: int) -> int:
        ref = [0 for _ in range(n+1)]
        ref[0] = ref[1] = 1
        
        if n < 0:
            return 0
        if n < 2:
            return ref[n-1]
        
        for i in range(2, n + 1):
            ref[i] = ref[i-1] + ref[i-2]

        return ref[n]