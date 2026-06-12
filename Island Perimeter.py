class Solution(object):
    def islandPerimeter(self, grid):
        counts = 0
        same_var = 0
        column = len(grid[0])
        transposed = [[0] * len(grid) for i in range(column)]
        for i in range(column):
            for j in range(len(grid)):
                transposed[i][j] = grid[j][i]
        for i in range(column):
            for j in range(1,len(grid)):
                if transposed[i][j] == 1 and transposed[i][j-1] == 1:
                    same_var += 1
        for i in range(len(grid)):
            for j in range(1,column):
                if grid[i][j] == 1 and grid[i][j-1] == 1:
                    same_var += 1
        for i in range(column):
            for j in range(len(grid)):
                if transposed[i][j] == 1:
                    counts += 1 
        return (counts * 4)  - (same_var *2)                                 


               
        
