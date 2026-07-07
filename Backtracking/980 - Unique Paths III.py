'''You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)'''



class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        sx,sy=0,0
        ic=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    sx,sy=i,j
                if grid[i][j]==-1:
                    ic+=1
        vc=(len(grid)*len(grid[0]))-ic
        c=0

        def backtrack(x,y,step):
            nonlocal c
            n=len(grid)
            m=len(grid[0])
            if x<0 or x>=n or y<0 or y>=m or grid[x][y]==-1:
                return
            if grid[x][y]==2:
                if step == vc:
                    c+=1
                return
            temp=grid[x][y]
            grid[x][y]=-1
            backtrack(x+1,y,step+1)
            backtrack(x,y+1,step+1)
            backtrack(x-1,y,step+1)
            backtrack(x,y-1,step+1)
            grid[x][y]=temp
            return
        
        backtrack(sx,sy,1)
        return c