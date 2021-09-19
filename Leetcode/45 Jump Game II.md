# 45. Jump Game II

Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: nums = [2,3,0,1,4]
Output: 2
```

**Constraints:**

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 105`

## Answer

首刷約 19分，DP解

Time: O(N^2) where N is the size of nums.

```python
# Runtime: 16 ms, faster than 96.38% of Python online submissions for Jump Game II.
# Memory Usage: 13.3 MB, less than 96.38% of Python online submissions for Jump Game II.
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sz = len(nums)
        dp = [float("inf")] * sz
        dp[0] = 0
        for i in xrange(1, sz):
            mn = float("inf")
            for j in xrange(i):
                if nums[j]+j >= i and mn > dp[j]:
                    mn = dp[j]
            dp[i] = mn+1
        return dp[sz-1]
        
'''
dp[j] = 
min{ dp[k] for k in xrange(j) if nums[k]+k >= j} + 1
'''
```