# 63. Unique Paths II
Q: A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

![img](imgs/63_1.png)


An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:
```
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

## Answer
最佳解是使用 DP
```python
# from: https://leetcode-cn.com/problems/unique-paths-ii/solution/shou-hua-tu-jie-dp-si-lu-by-hyj8/

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        grid = obstacleGrid
        w = len(grid[0])
        h = len(grid)
        
        grid[0][0] = 1 if grid[0][0] == 0 else 0
        for i in xrange(1, w):
            grid[0][i] = 1 if grid[0][i-1] == 1 and grid[0][i] == 0 else 0
        
        for i in xrange(1, h):
            grid[i][0] = 1 if grid[i-1][0] == 1 and grid[i][0] == 0 else 0
            
        for m in xrange(1, h):
            for n in xrange(1, w):
                if grid[m][n] == 1:
                    grid[m][n] = 0
                else:
                    grid[m][n] = grid[m-1][n] + grid[m][n-1]
                    
        return grid[h-1][w-1]
        
#        
# 如果使用 DFS法 會超時
#
#         grid = obstacleGrid
#         w = len(grid[0])
#         h = len(grid)
#         r = [0]
#         def dfs(y, x):
#             if y == h or x == w or grid[y][x] == 1:
#                 return
            
#             if y == h-1 and x == w-1:
#                 r[0] += 1
            
#             dfs(y+1, x)
#             dfs(y, x+1)
            
#         dfs(0, 0)
#         return r[0]
```