# 994. Rotting Oranges

Q: In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
```
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```
Example 2:
```
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

Example 3:
```
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
```
 
Note:
```
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
```

## 思路
使用到 [List/Set/Dictionary Comprehension](https://zh.wikipedia.org/wiki/List_comprehension) ([Other resource](https://yuchungchuang.wordpress.com/2017/08/16/python-%E4%B8%B2%E5%88%97%E7%B6%9C%E5%90%88%E8%A1%A8%E9%81%94%E5%BC%8F-list-comprehension/))

## Answer
Jeff 2 刷 (約50分) (BFS)
```python
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isFresh(cell):
            (i, j) = (cell[0], cell[1])
            if i < 0 or j < 0 or i >= h or j >=w:
                return False
            
            if grid[i][j] == 1:
                grid[i][j] = 2
                return True
            else:
                return False
        
        h = len(grid)
        w = len(grid[0])
        
        dq = deque()
        
        hasOne = False
        for i in xrange(h):
            for j in xrange(w):
                if grid[i][j] == 2:
                    dq.appendleft((i, j))
                elif grid[i][j] == 1:
                    hasOne = True

        if not hasOne:
            return 0
        
        ans = -1
        while dq:
            for x in xrange(len(dq)):
                (i, j) = dq.pop()
                cell = (i+1, j)
                if isFresh(cell):
                    dq.appendleft(cell)
                cell = (i-1, j)
                if isFresh(cell):
                    dq.appendleft(cell)
                cell = (i, j+1)
                if isFresh(cell):
                    dq.appendleft(cell)
                cell = (i, j-1)
                if isFresh(cell):
                    dq.appendleft(cell)
            ans += 1
            
        for i in xrange(h):
            for j in xrange(w):
                if grid[i][j] == 1:
                    return -1
        return ans
```

高手解 (Set)
```python
class Solution:
    def orangesRotting(self, grid):
        row, col = len(grid), len(grid[0])
        rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        timer = 0
        while fresh:
            if not rotting: return -1
                                                                     # 這裡用 [...]或 {...} 都可以
            rotting = {(i+di, j+dj) for i, j in rotting for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i+di, j+dj) in fresh}
            fresh -= rotting
            timer += 1
        return timer
```


Jeff's First (BFS) (Novice code XD)
```python
from Queue import Queue
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        q = Queue()
        
        w = len(grid[0])
        h = len(grid)
        
        fresh = 0
        for x in xrange(w):
            for y in xrange(h):
                if grid[y][x] == 2:
                    q.put((y, x))
                elif grid[y][x] == 1:
                    fresh += 1

        q.put((-1, -1))
                   
        r = 0
        while not q.empty():
            t = q.get()
            
            x = t[1]
            y = t[0]
            
            if x == -1:
                if not q.empty():
                    q.put((-1, -1))
                    r += 1
                continue
            
            y -= 1     
            if y >= 0:
                self.update(q, grid, x, y)
                    
            y = t[0]
            x -= 1
            if x >= 0:
                self.update(q, grid, x, y)

            x = t[1]
            y = t[0] + 1
            if y < h:
                self.update(q, grid, x, y)
                
            x = t[1] + 1
            y = t[0]
            if x < w:
                self.update(q, grid, x, y)
                
        for y in xrange(h):
            for x in xrange(w):
                if grid[y][x] == 1:
                    return -1
                
        return r
        
        
    def update(self, q, grid, x, y):
        if grid[y][x] == 1:
            grid[y][x] = 2
            q.put((y, x))

s = Solution()
print s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
print s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
```