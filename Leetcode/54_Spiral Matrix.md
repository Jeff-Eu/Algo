# 54. Spiral Matrix
Q: Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

1 2 3
4 5 6
7 8 9
```
Example 2:
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

1  2  3  4
5  6  7  8
9 10 11 12
``` 

## Answer

首刷約 90分 
```python
# Runtime: 12 ms, faster than 94.00% of Python online submissions for Spiral Matrix.
# Memory Usage: 13.6 MB, less than 6.32% of Python online submissions for Spiral Matrix.
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        out=[]
        w = len(matrix[0])
        h = len(matrix)
        
        def delta(n):
            n=n%4
            
            if n==1:
                return (0, 1)
            elif n==2:
                return (1, 0)
            elif n==3:
                return (0, -1)
            else:
                return (-1, 0)
            
        def dfs(i, j, n):
            
            if i >= h or i < 0 or j >= w or j < 0 or matrix[i][j] == '#':
                return False
            
            out.append(matrix[i][j])
            matrix[i][j] = '#'
            dy, dx = delta(n)
            y, x = i+dy, j+dx
            
            k=0 # very very important !!!
            
            while k != 4 and not dfs(y, x, n):
                n += 1
                k += 1
                dy, dx = delta(n)
                y, x = i+dy, j+dx                
                
            return True
                
        dfs(0, 0, 1)
        return out
```