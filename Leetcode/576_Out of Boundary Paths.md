# 576. Out of Boundary Paths

There is an `m x n` grid with a ball. The ball is initially at the position `[startRow, startColumn]`. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply **at most** `maxMove` moves to the ball.

Given the five integers `m`, `n`, `maxMove`, `startRow`, `startColumn`, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it **modulo** `109 + 7`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_1.png)

**Input:** m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
**Output:** 6

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_2.png)

**Input:** m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
**Output:** 12

**Constraints:**

-   `1 <= m, n <= 50`
-   `0 <= maxMove <= 50`
-   `0 <= startRow < m`
-   `0 <= startColumn < n`

## Answer
Memoization

```python
# Runtime: 107 ms, faster than 84.62% of Python online submissions for Out of Boundary Paths.
# Memory Usage: 19 MB, less than 33.33% of Python online submissions for Out of Boundary Paths.
class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        mem = {}
        def getPaths(mxMove, row, col):
            if (row, col, mxMove) in mem:
                return mem[(row, col, mxMove)]
                        
            if row==-1 or row==m or col==-1 or col==n:
                return 1
            
            if mxMove==0:
                return 0

            out = mem[(row, col, mxMove)] = getPaths(mxMove-1, row-1, col) + getPaths(mxMove-1, row+1, col) + getPaths(mxMove-1, row, col-1) + getPaths(mxMove-1, row, col+1)
            return out    
        
        big = 1000000007
        return getPaths(maxMove, startRow, startColumn) % big
```

Time complexity : O(mnN). We need to fill the memo array once with dimensions m x n x N. Here, m, n refer to the number of rows and columns of the given grid respectively. N refers to the total number of allowed moves.
Space complexity : O(mnN). memo array of size m x n x N is used.

這題的進階版是 [[688_Knight Probability in Chessboard]] 


#medium 