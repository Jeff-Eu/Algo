# 131. Palindrome Partitioning
Q: Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:
```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```
Example 2:
```
Input: s = "a"
Output: [["a"]]
```
## Answer
1天後複刷: 8分鐘

其實這題的作法跟過去 Permutations 或是 Combinations 的作法很像。

* 看過論譠的解法後複刷約30分，卡在 for 迴圈終止的地方寫錯
* python 3:
    * 函式回傳型態可寫可不寫
    * 記得迴圈是用 range，不是 xrange，乾脆以後 Python 2也用 range就好
    * print("hello") instead of print "hello"

```python 3
# Runtime: 648 ms, faster than 76.32% of Python3 online submissions for Palindrome Partitioning.
# Memory Usage: 30.2 MB, less than 50.51% of Python3 online submissions for Palindrome Partitioning.
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPal(s1: str) -> bool:
            return s1 == s1[::-1] # 雖然沒有很快，但簡潔易懂
        
        def dfs(s1, path):
            if not s1:
                out.append(path)
            
            size1 = len(s1)
            for i in range(1, size1+1):  # 注意這邊是到 size1 + 1，不小心會寫成 size1
                part = s1[:i]
                if isPal(part):
                    dfs(s1[i:], path+[part])
        
        out = []
        dfs(s, [])
        return out
```