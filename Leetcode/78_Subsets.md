# 78. Subsets
Q: Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]

Output:
```
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

## Answer
77題的延伸版，會77題接著再做這題約花15分
```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(index, pick, arr, n):
            if pick >= n:
                r.append(arr)
                return

            for i in xrange(index, size):
                # 在77題當作加速用，但這似乎效用不大                
                # if i-1+n-pick >= size:
                #     break
                
                dfs(i+1, pick+1, [nums[i]]+arr, n)
                
        r=[]
        r.append([])
        size = len(nums)
        for i in xrange(1, size+1):
            dfs(0, 0, [], i)

        return r
```

詳解有一個很漂亮的解法，Cascading Approach:
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output
```