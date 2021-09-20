# 498. Diagonal Traverse
Q: Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

![](imgs/498.png)

## Answer

有想到一個方法解這題(應該跟詳解1相同)，但實作上code有點多如下，整個時間花了約1小時，中間有做過一些優化，所以出了兩版，最終版是 90%以上的解。

* 發現在解 2D 問題的時候，常會需要從 2D Matrix 去觀察，就容易找到解法，學習看著 2D Matrix 觀察或作圖、舉例。

首刷最終版:
```python
# Runtime: 156 ms, faster than 95.33% of Python online submissions for Diagonal Traverse.
# Memory Usage: 16.4 MB, less than 86.65% of Python online submissions for Diagonal Traverse.
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        def getNextPos(i, j):
            x = j-1
            y = i+1
            return (y, x)
        
        w = len(matrix[0])
        h = len(matrix)
        
        out = []
        up = False
        for j in xrange(w):
            i = 0
            up = not up
            size = len(out)
            while i<h and j>=0:
                if not up:
                    out.append(matrix[i][j])
                else:
                    out.insert(size, matrix[i][j])
                (i, j) = getNextPos(i, j)
                
        for i in xrange(1, h):
            j = w-1
            up = not up
            size = len(out)
            while i<h and j>=0:
                if not up:
                    out.append(matrix[i][j])
                else:
                    out.insert(size, matrix[i][j])
                (i, j) = getNextPos(i, j)
            
        return out    
```

首刷初版:
```python
# Runtime: 176 ms, faster than 51.67% of Python online submissions for Diagonal Traverse.
# Memory Usage: 16.3 MB, less than 86.65% of Python online submissions for Diagonal Traverse.
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def getNextPos(i, j):
            x = j-1
            y = i+1
            return (y, x)
        
        if not matrix:
            return []
        
        w = len(matrix[0])
        h = len(matrix)
        
        out = []
        up = False
        for j in xrange(w):
            i = 0
            part = []
            up = not up
            while i<h and j>=0:
                part.append(matrix[i][j])
                (i, j) = getNextPos(i, j)
            
            if not up:
                out += part
            else:
                out += part[::-1]
                
        for i in xrange(1, h):
            j = w-1
            part = []
            up = not up
            while i<h and j>=0:
                part.append(matrix[i][j])
                (i, j) = getNextPos(i, j)
                
            if not up:
                out += part
            else:
                out += part[::-1]
            
        return out
'''reasoning
1 2 3 4
5 6 7 8

1 2 5 6 3 4 7 8
1 2 5 3 6 4 7 8

 1  2  3  4  5 
 6  7  8  9  10
11 12 13 14  15
'''
'''reasoning
1 2 3 4
5 6 7 8

1 2 5 6 3 4 7 8
1 2 5 3 6 4 7 8

 1  2  3  4  5 
 6  7  8  9  10
11 12 13 14  15
'''
```
