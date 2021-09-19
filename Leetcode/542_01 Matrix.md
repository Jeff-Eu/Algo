# 542. 01 Matrix
Q: Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
```
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
```
Example 2:
```
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
```
## Answer

一開始用 DFS的方法去寫，結果submit會超時，中間加了一些加速的判斷還是超時。
```python
# DFS: Time Exceeded
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def getMinDis(m, n, minDiff):
            if m<0 or n<0 or m>=h or n>=w or matrix[m][n] == 2:
                return float("inf")
            
            if matrix[m][n] == 0:
                return 0
            
            if out[m][n] != -1:
                return out[m][n]
            
            if minDiff == 0:
                return float("inf")
            
            tmp = matrix[m][n]
            matrix[m][n] = 2
            
            r = float("inf")
            
            for i in xrange(2):
                for j in [1, -1]:
                    if i==0:
                        v = 1 + getMinDis(m+j, n, r-1)
                        r = min(r, v)
                    else:
                        v = 1 + getMinDis(m, n+j, r-1)
                        r = min(r, v)
                
            matrix[m][n] = tmp
            return r
        
        h = len(matrix)
        w = len(matrix[0])
        out = [[-1]*w for _ in xrange(h)]
        
        for i in xrange(h):
            for j in xrange(w):
                out[i][j] = getMinDis(i, j, float("inf"))
                
        return out
```

後來瞄了詳解的標題一下，才發現我的DFS算是詳解的第一種方法，應該要用第二種BFS才不會超時，後來就自己嘗試寫出來。

一刷。另外配置額外的陣列，自己評估 Time: O(wh)
```python
# BFS: Pass
# Runtime: 604 ms, faster than 70.33% of Python online submissions for 01 Matrix.
# Memory Usage: 16.7 MB, less than 67.06% of Python online submissions for 01 Matrix.
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        h = len(matrix)
        w = len(matrix[0])
        out = [[-1]*w for _ in xrange(h)]
        
        def getDis(m, n):
            st = set()
            dq = deque()
            p = (m, n)
            dq.append(p)
            st.add(p)
            dis = 0
            while dq:
                sz = len(dq)
                dis += 1
                for k in xrange(sz):
                    (m, n) = dq.popleft()

                    for i in xrange(2):
                        for j in [1, -1]:
                            if i==0:
                                p = (m+j, n)
                            else:
                                p = (m, n+j)
                            
                            if p in st or p[0]<0 or p[1]<0 or p[0]>=h or p[1]>=w:
                                continue
                                
                            if matrix[p[0]][p[1]]==1:
                                dq.append(p)
                                st.add(p)
                            else: # 0
                                return dis
            return 0
        
        for i in xrange(h):
            for j in xrange(w):
                if matrix[i][j] == 0:
                    out[i][j] = 0
                else:
                    out[i][j] = getDis(i, j)

        return out
'''
0 1 1 1
1 1 1 0
1 1 1 1
1 1 1 1
   3
  323
 32123
3210123
 32123
  323
   3

'''
```

## 新技能
* 2D陣列或3D陣列存取的精簡寫法：
	* 遇到2D陣列的上下左右需要access時，可以用下面這種寫法
		```python
		for j in xrange(2):
			for k in [1, -1]:
				if j==0:
					p = (m+k, n)
				else:
					p = (m, n+k)
		```
	* 同理，在3維空間中需要access上下左右前後，可以用下面這種寫法
		```python
		for i in xrange(3):
			for j in [1, -1]:
				if i==0:
					p = (a+j, b, c)
				elif i==1:
					p = (a, b+j, c)
				else:
					p = (a, b, c+j)
		```

## Review

後來又仔細看了一下詳解的BFS方法，發現它從 0 開始往外擴張，降比較聰明，就不用額外再配置相同大小的陣列，所以自己實作了一次，比一刷的BFS還精簡。

Time: O(w*h) 
```python
# Runtime: 644 ms, faster than 59.64% of Python online submissions for 01 Matrix.
# Memory Usage: 16.3 MB, less than 71.81% of Python online submissions for 01 Matrix.
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        h = len(matrix)
        w = len(matrix[0])
        q = deque()
        for i in xrange(h):
            for j in xrange(w):
                if matrix[i][j] == 1:
                    matrix[i][j] = -1
                else: # 0
                    q.append((i, j))
            
        dis = 0
        while q:
            size = len(q)
            dis += 1
            for i in xrange(size):
                (m, n) = q.popleft()
                
                for j in xrange(2):
                    for k in [1, -1]:
                        if j==0:
                            p = (m+k, n)
                        else:
                            p = (m, n+k)
                            
                        if p[0]<0 or p[1]<0 or p[0]>=h or p[1]>=w or matrix[p[0]][p[1]] != -1:
                            continue
                            
                        matrix[p[0]][p[1]] = dis # 注意，設dis要寫在這，不能寫在 q.popleft()的後面，才不會被重覆設
                        q.append(p)
        return matrix
                        
'''
0 1 1 1
1 1 1 0
1 1 1 1
1 1 1 1
   3
  323
 32123
3210123
 32123
  323
   3
'''
```