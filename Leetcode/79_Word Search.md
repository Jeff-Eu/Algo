# 79. Word Search
Q: Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:
```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
```
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

## Answer
複刷 
實用小技巧：        
    h = len(board)
    w = len(board[0])
```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, k):
            
            if i < 0 or j < 0 or i >= h or j >= w:
                return False
            
            if (i, j) in hsh:
                return False
            
            if board[i][j] != word[k]:
                return False
            else:
                
                hsh.add((i, j))
                if k == sz[0]-1:
                    return True
            
            b = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            if b == False:
                hsh.remove((i, j))
            return b
            
        h = len(board)
        w = len(board[0])
        
        sz = [len(word)]
        hsh = set()

        for i in xrange(h):
            for j in xrange(w):
                if dfs(i, j, 0) == True:
                    return True
                
        return False
```

```python
# 90分鐘
# Runtime: 288 ms, faster than 90.63% of Python online submissions for Word Search.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(index, m, n):
            if board[m][n] != word[index]:
                return False
            elif (m,n) in traced:
                return False
            else:
                if index >= size-1:
                    return True
                
                # mark the cell as traversed
                traced.add((m,n))

                if m > 0:
                    if dfs(index+1, m-1, n):
                        return True
                if m < h-1:
                    if dfs(index+1, m+1, n):
                        return True
                if n > 0:
                    if dfs(index+1, m, n-1):
                        return True
                if n < w-1:
                    if dfs(index+1, m, n+1):
                        return True
                    
                traced.remove((m,n))
                return False


        h = len(board)
        w = len(board[0])
        size = len(word)
        traced = set()
        for m in xrange(h):
            for n in xrange(w):
                if board[m][n] == word[0]:
                    if dfs(0, m, n):
                        return True
        return False 
```
