# 212. Word Search II
Q: Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:

![](imgs/212_1.jpg)
```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```
Example 2:

![](imgs/212_2.jpg)
```
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```
## Answer
會做 79. Word Search 的話，這題就只需要再加一點東西就可解出(但還是比較難)。

兩個技巧：
* python的 set轉 list ==> list({2, 3})
* 參考下面code的 word 及 size，可以被 dfs 的函式所取用，代表若該變數名稱沒被override的話，在它的 life scope 中，local function 還是能看到([這算python closure的性質](http://zetcode.com/python/python-closures/#:~:text=A%20closure%20is%20a%20nested,it%20is%20a%20nested%20function))；但如果是 method就看不到了。
    * 記得 local function 都寫在最前面，後面要呼叫時才看得到。

```python
# Runtime: 24 ms, faster than 82.02% of Python online submissions for Word Search II.
# Memory Usage: 13.6 MB, less than 80.38% of Python online submissions for Word Search II.
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
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
        sett = set()
        for word in words:
            size = len(word)
            traced = set()
            for m in xrange(h):
                for n in xrange(w):
                    if board[m][n] == word[0]:
                        if dfs(0, m, n):
                            sett.add(word)
        return list(sett)
```