#Leetcode DFS question

class Solution():
    def minPathSum(self, grid):
        least_sum = []
        visited = []
    
        def DFS(grid, total, i, j):
            flag = 0
            total += grid[i][j]
            visited.append((i,j))
        
            if (i == len(grid) - 1 and j == len(grid[0]) -1):
                least_sum.append(total)
                return
          
            #move down    
            if (len(grid) > i+1 >= 0):
                for k in visited:
                    if ((i+1,j) == visited):
                        flag = 1
                if (flag == 0):
                    DFS(grid, total, i+1, j)
        
            #move right
            if (len(grid[0]) > j+1 >= 0):
                for k in visited:
                    if ((i+1,j) == visited):
                        flag = 1
                if (flag == 0):
                    DFS(grid, total, i, j+1)
        
        
        DFS(grid, 0, 0, 0)
        minim = min(least_sum)
        #print least_sum
        print minim
        

test = Solution()

arr = [[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]]
test.minPathSum(arr)