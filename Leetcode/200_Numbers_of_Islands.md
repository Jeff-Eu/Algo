# 200. Number of Islands
Q: Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

```
Input:
11110
11010
11000
00000

Output: 1
```
Example 2:
```
Input:
11000
11000
00100
00011

Output: 3
```
## Answer
2刷被陷阱超時，陣列裡面存的不是0，是"0"，甘！本來可以在15分鐘寫出來的。

```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(m, n):
            if m<0 or n<0 or m==h or n==w:
                return False
            
            if grid[m][n] == "0":
                return False
            
            grid[m][n] = "0"
            
            dfs(m-1, n)
            dfs(m, n+1)
            dfs(m+1, n)
            dfs(m, n-1)
            return True
            
        h = len(grid)
        w = len(grid[0])
        out = 0
        for i in xrange(h):
            for j in xrange(w):
                if dfs(i, j):
                    out += 1
        return out
```


Jeff's: HashSet + BFS ( Faster than 91.77%. Memory less than 9.46% )
```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # avoid the boundary case, grid == []
        if not grid:
            return 0
        
        w, h = len(grid[0]), len(grid)
        land = {(y, x) for y in xrange(h) for x in xrange(w) if grid[y][x] == "1"}
        
        num = 0
        while land:
            # note here ! spread must be a set
            spread = { next(iter(land)) }
            num += 1
            while spread:
                land -= spread            
                spread = {(y+dy, x+dx) for y, x in spread for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)] if (y+dy, x+dx) in land}
                
        return num
                

s = Solution()
print s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
```

學平's:  ( Faster than 92.76%. Memory less than 41.94% )

用迴圈跑一輪，找到'1'就用DFS開始搜尋，在DFS遍歷的時候找到'1'便把該位置設為'0'直到遞迴結束，並把結果數目+1。

```javascript
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    var colLength = grid.length;
    var count = 0;
    if (colLength === 0) return 0;
    var rowLength = grid[0].length;
    
    var DFS = function(grid, x, y) {
        if (x < 0 || y < 0 || x >= colLength || j >= rowLength || grid[x][y] !== '1') return;
        
        grid[x][y] = '0';
        
        DFS(grid, x + 1, y);
        DFS(grid, x - 1, y);
        DFS(grid, x, y + 1);
        DFS(grid, x, y - 1);
    }
    
    for (var i = 0; i < colLength; i++) {
        for (var j = 0; j < rowLength; j++) {
              if (grid[i][j] === '1') {
                  DFS(grid, i, j);
                  ++ count;
              }
        }
    }
    
    return count;
};
```