class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if int(grid[row][col]) == 1:
                    count+=1
                self.helper(row, col, grid)
                
        return count
    
    def helper(self, row, col, grid):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and int(grid[row][col]) == 1:
            grid[row][col] = 0
            
            self.helper(row+1, col, grid)
            self.helper(row, col+1, grid)
            self.helper(row-1, col, grid)
            self.helper(row, col-1, grid)