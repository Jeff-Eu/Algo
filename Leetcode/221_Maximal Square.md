# 221. Maximal Square
Q: Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
```
Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
```
## 思路
這題沒有寫做過的話很難想得到怎麼解，不過一旦知道它的DP解法原理之後，就很容易記下來在下次迎刃而解。

看詳解的圖就很容易回想起來，或是看[這影片的教學，特別是在影片19:50的地方](https://www.youtube.com/watch?v=FO7VXDfS8Gk)

## 英文補充
* This can be easier to depict by drawing.
*

## Answer
Jeff 覆刷(看過前面的影片後)
```python 3
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        h = len(matrix)
        w = len(matrix[0])
        
        arr = [[0] * w for _ in range(h)]
        ans = 0
        for i in range(h):
            for j in range(w):
                if i==0 or j == 0:
                    arr[i][j] = int(matrix[i][j])
                elif matrix[i][j] != '0':
                    arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1

                ans = max(arr[i][j], ans)

        return ans * ans
```

Jeff's 一刷(較易懂)
```python
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        w = len(matrix[0])
        h = len(matrix)
        
        cache = []
        for i in xrange(h):
            cache.append([])
            for j in xrange(w):
                if matrix[i][j] == "0":
                    cache[i].append(0)
                else:
                    cache[i].append(1)
        
        side = 0
        for i in xrange(h):
            for j in xrange(w):
                if i != 0 and j != 0 and matrix[i][j] == "1":
                    cache[i][j] = min(cache[i-1][j], cache[i-1][j-1], cache[i][j-1]) + 1
                    
                side = max(side, cache[i][j])
                
        return side*side
```

Jeff's 二刷(效率比一刷好一點):
```python
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        w = len(matrix[0])
        h = len(matrix)
        
        cache = []
        
        side = 0
        for i in xrange(h):
            cache.append([])
            for j in xrange(w):
                if i != 0 and j != 0 and matrix[i][j] == "1":
                    cache[i].append(min(cache[i-1][j], cache[i-1][j-1], cache[i][j-1]) + 1)
                else:
                    cache[i].append(0 if matrix[i][j] == "0" else 1)
                 
                if cache[i][j] > side: side = cache[i][j]
                
        return side*side
```