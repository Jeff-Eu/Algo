# 22. Generate Parentheses
Q: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

## Answer
Jeff 2刷:\
```python
# Runtime: 20 ms, faster than 79.50% of Python online submissions for Generate Parentheses.
# Memory Usage: 13.6 MB, less than 68.28% of Python online submissions for Generate Parentheses.
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r = []
        def dfs(s,left,right):
            if left==n and right==n:
                r.append(s)
                return
            if left > n: # or right > n:
                return
            
            dfs(s+"(", left+1, right)
            if left > right:
                dfs(s+")", left, right+1)
            
        dfs("",0,0)
        return r
```

高手解 (Backtracking):
```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        out = []
        def backtrack(s = "", left = 0, right = 0):
            if len(s) == n*2:
                out.append(s)
                return
            if left > right:
                backtrack(s+")", left, right+1)
            if left < n:
                backtrack(s+"(", left+1, right)
            
        backtrack()
        return out
```