# 46. Permutations
Q: Given a collection of distinct integers, return all possible permutations.

Example:
```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

## Answer
高手解:
Solution 1: Recursive, take any number as first
```python
# Runtime: 32 ms, faster than 38.62% of Python online submissions for Permutations.
# Memory Usage: 13.7 MB, less than 42.80% of Python online submissions for Permutations.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        out = []
        def dfs(nums, perm):
            if not nums:
                out.append(perm)
                
            for i in xrange(len(nums)):
                dfs(nums[:i]+nums[i+1:], perm+[nums[i]])
                
        dfs(nums, [])
        return out
```

三刷，類似 Solution 1 的 Recursive, take any number as first，但是比較好想像的做法
```python
# Runtime: 24 ms, faster than 89.70% of Python online submissions for Permutations.
# Memory Usage: 13.9 MB, less than 5.13% of Python online submissions for Permutations.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(path, st1):
            if not st:
                ans.append(path)
                return
            
            st2 = set(st1)
            for v in st2:
                st1.remove(v)
                dfs(path + [v], st1)
                st1.add(v)
        
        ans = []
        st = set(nums)
        dfs([], st)
            
        return ans
```
改良上面，將 set 換成 list 後如下
```python
# Runtime: 20 ms, faster than 98.25% of Python online submissions for Permutations.
# Memory Usage: 13.8 MB, less than 18.40% of Python online submissions for Permutations.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(path, ls):
            if not ls:
                ans.append(path)
                return
            
            for i in xrange(len(ls)):
                v = ls.pop(i) # 刪除特定index要用pop，不是remove
                dfs(path + [v], ls)
                ls.insert(i, v)
        
        ans = []
        dfs([], nums)
            
        return ans
```
不過 insert()及 pop()在 python 的 list 都是 O(N)時間，Python 有可以額外安裝的libary叫作 [blist](https://stackoverflow.com/questions/27073596/what-is-the-cost-complexity-of-insert-in-list-at-some-location/27073672#27073672)，能提供O(logN)時間


Solution 2 (harder):\
Recursive, insert first number anywhere
```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []
        for i in range(len(nums)):
            for p in self.permute(nums[1:]): # P needs to be array, that's why return [[]] when nums == []
                out.append(p[:i] + [nums[0]] + p[i:])
              
        if nums == []:
            return [[]]
        else:
            return out
```
Jeff's 一刷:\
Solution 2: Recursive, insert first number anywhere
```python
# Runtime: 24 ms, faster than 87.47% of Python online submissions for Permutations.
# Memory Usage: 13 MB, less than 6.00% of Python online submissions for Permutations.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        size = len(nums)
        out = []

        def doit(ni, perm):
            for i in xrange(size):
                if perm[i] == None:
                    perm[i] = nums[ni]
                    if ni+1 < size:
                        doit(ni+1, perm[:])
                        perm[i] = None
                    else:
                        out.append(perm)
                  
        doit(0, [None]*size)
        return out
```