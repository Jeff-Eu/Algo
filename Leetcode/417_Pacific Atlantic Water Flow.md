# 417. Pacific Atlantic Water Flow
Q: Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.

Example:

Given the following 5x5 matrix:
```
  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic
```
Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

## Answer
想到 bottom-up的 DP 解法後，約在 20分內寫出

觀念：
* 對於落在 cell(i, j)的水，能往鄰近四方向是同高度或較矮的 cell 流動
* 若水可以從 A 流向 B，將它表示成 A->B  
    * 若 B 可流向某一 kind 的海洋，則 A 亦可流向它，因為 A 會流向 B
        * 因此，上面已建立出 DP 的關係
            * A->B 是水流的方向(往等高或較低流)，DP的關係則是 B=>A；而非 A=>B，也就是說，若A比B高，就算 A 已知流向某海洋 O1，則 B **不一定**也會流向 O1 !! ( 陷阱： A->B 容易誤解成 B 也會流進去) 反之若是 B 已知流向某海洋 O2，則 A 一定也會流進 O2
        * 我們從已知接觸某 kind 海洋的全部 cells 往四周去使用 DFS 回溯出其他的有流向該海洋的全部 cells，這些 cells 就會是 matrix 中全部流向該每洋的 cells (所以不會有其他 cells 會再流向該海洋了)
        * 為了方便計算，能不能只宣告一個同樣長寬的陣列，裡面的 cell 就能記錄可以流向那些 kind 的海洋呢？
            * 很簡單，只要透過 bitwise operation 的輔助即可, e.g.
                * 用 1 表示流向 Atlantic Ocean，用 2 表示流向 Pacific Ocean
                    * 初始值為 cell = 0，則可以用 cell |= 1 或 cell |= 2 來更新該 cell 是否可流向某 kind 的海洋，因此可寫成 cell |= kind
                        * 若 cell == 3 代表可流向兩種海洋
                        * if (cell & kind) == kind 代表該 cell 已經被算過，因此不再繼續後續運算，直接 return，如此可防止無窮迴圈

Bottom-up 完全DP (不用考慮全部 matrix 的 cell)
```python
# Runtime: 236 ms, faster than 90.74% of Python online submissions for Pacific Atlantic Water Flow.
# Memory Usage: 16.8 MB, less than 9.72% of Python online submissions for Pacific Atlantic Water Flow.
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(i, j, kind):
            if i<0 or j<0 or i>h-1 or j>w-1:
                return
            
            if (mem[i][j] & kind) == kind:
                return
            
            mem[i][j] |= kind
            
            v = matrix[i][j]
            if j>0 and matrix[i][j-1] >= v:
                dfs(i, j-1, kind) # left
                
            if i>0 and matrix[i-1][j] >= v:
                dfs(i-1, j, kind) # up
            
            if j<w-1 and matrix[i][j+1] >= v:
                dfs(i, j+1, kind) # right
            
            if i<h-1 and matrix[i+1][j] >= v:
                dfs(i+1, j, kind) # down
        
        if not matrix:
            return []
        
        h = len(matrix)
        w = len(matrix[0])
        
        # Bitwise operation will be applied into every cell in the mem.
        mem = [[0]*w for _ in xrange(h)]
        
        # 1 represents Pacific ocean
        for x in xrange(w):
            dfs(0, x, 1)
            
        for y in xrange(h):
            dfs(y, 0, 1)
            
        # 2 represents Atlantic ocean
        for x in xrange(w):
            dfs(h-1, x, 2)
            
        for y in xrange(h):
            dfs(y, w-1, 2)
            
        out = []
        for i in xrange(h):
            for j in xrange(w):
                if mem[i][j] == 3:
                    out.append([i, j])
        return out
```


Top-down 不完全DP (待解釋)，全部 matrix 的 cell 都計算了
```python
# Runtime: 932 ms, faster than 8.56% of Python online submissions for Pacific Atlantic Water Flow.
# Memory Usage: 15.1 MB, less than 90.97% of Python online submissions for Pacific Atlantic Water Flow.
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(m, n, isOrigin):
            if m < 0 or n < 0 or m >= h or n >= w:
                return 0
            
            if mem[m][n] != -1:
                return mem[m][n]
            
            x=0
            v = matrix[m][n]
            matrix[m][n] = -1
            if m == 0 or n == 0:
                x |= 1
                
            if m == h-1 or n == w-1:
                x |= 2
                
            # left
            if x != 3 and n > 0 and matrix[m][n-1] <= v and matrix[m][n-1] != -1:
                x |= dfs(m, n-1, False)
            # up
            if x != 3 and m > 0 and matrix[m-1][n] <= v and matrix[m-1][n] != -1:
                x |= dfs(m-1, n, False)
            # right
            if x != 3 and n < w-1 and matrix[m][n+1] <= v and matrix[m][n+1] != -1:
                x |= dfs(m, n+1, False)
            # down
            if x != 3 and m < h-1 and matrix[m+1][n] <= v and matrix[m+1][n] != -1:
                x |= dfs(m+1, n, False)
                        
            if isOrigin or x == 3:
                mem[m][n] = x

            matrix[m][n] = v
            
            return x
        
        if not matrix:
            return []
        
        h = len(matrix)
        w = len(matrix[0])
                
        # Pacific: | 1 ;  Atlantic: | 2
        # if cell == 3 then the cell can flow to both oceans
        mem = [[-1]*w for _ in xrange(h)]
        out = []
        for i in xrange(h):
            for j in xrange(w):
                if dfs(i, j, True) == 3:
                    out.append([i, j])
        return out
```