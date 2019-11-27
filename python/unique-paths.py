class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        weights = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(m):
            weights[0][i] = 1
            
        for i in range(n):
            weights[i][0] = 1
        
        for row in range(1,n):
            for col in range(1,m):
                weights[row][col] += weights[row - 1][col] + weights[row][col - 1]
                
        return weights[n-1][m-1]