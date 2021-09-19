# 47. Permutations II
Q: Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
```
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```
## Answer
46題 Permutations 的進階版，只要會46的第一種解法，稍微改一下這題就能迎刃而解
```python
# Runtime: 40 ms, faster than 97.09% of Python online submissions for Permutations II.
# Memory Usage: 13.7 MB, less than 70.42% of Python online submissions for Permutations II.
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []
        
        def doit(perm, left):
            if not left:
                out.append(perm)
            
            _set = set()
            size = len(left)
            for i in xrange(size):
                if left[i] not in _set:
                    _set.add(left[i]) # 注意這邊不用特別為 left 做 sort
                    doit(perm + [left[i]], left[:i] + left[i+1:])
            
        doit([], nums)
        return out
```

二刷改良
```python
# Runtime: 40 ms, faster than 97.09% of Python online submissions for Permutations II.
# Memory Usage: 13.9 MB, less than 12.02% of Python online submissions for Permutations II.
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(path, ls):
            if not ls:
                ans.append(path)
                return
            
            st = set()
            for i in xrange(len(ls)):
                if ls[i] in st:
                    continue
                
                v = ls.pop(i) # 刪除特定index要用pop，不是remove
                st.add(v)
                dfs(path + [v], ls)
                ls.insert(i, v)
        
        ans = []
        dfs([], nums)
            
        return ans
```