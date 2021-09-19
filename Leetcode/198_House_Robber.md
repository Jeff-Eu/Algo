# 198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
```
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```
Example 2:
```
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
```

## Answer
觀念，Based on the recursive formula:

> f(0) = nums[0]\
> f(1) = max(num[0], num[1])\
> f(k) = max( f(k-2) + nums[k], f(k-1) )

[論譠裡也有其他很好的解釋](https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.)

看過上面公式後2.5刷：Top down approach (Iterative)
```python
# Runtime: 16 ms, faster than 84.77% of Python online submissions for House Robber.
# Memory Usage: 13.5 MB, less than 15.28% of Python online submissions for House Robber.
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        elif size == 1:
            return nums[0]
        elif size == 2:
            return max(nums[0], nums[1])
        
        last2 = nums[0]
        last = max(nums[0], nums[1]) # 小心這邊別寫成 last = nums[1]
        out = 0
        for i in xrange(2, size):
            out = max(last2 + nums[i], last)
            last2 = last
            last = out
        return out
```

二刷(約40分，沒看解答) (Bottom up - Recursive DP)
```python
# Runtime: 212 ms, faster than 5.80% of Python online submissions for House Robber.
# Memory Usage: 13.5 MB, less than 15.28% of Python online submissions for House Robber.
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        mem = [-1]*size
        def getMax(idx):
            if mem[idx] != -1:
                return mem[idx]
            
            # 注意2點，一開始一直寫錯 (注意邏輯，而非套招)
            # 1. 初始值 out跟 lm 不能設為 0
            out = lm = nums[idx]
            for i in xrange(idx, size):
                for j in xrange(i+2, size):
                    lm = nums[i] + getMax(j)  # 2. 不能寫成 lm += getMax(j)，否則 lm 一直遞增上去
                    if lm > out:
                        out = lm
            mem[idx] = out
            return out
            
        amax = 0
        lmax = 0
        for i in xrange(size):
            lmax = getMax(i)
            if lmax > amax:
                amax = lmax
                
        return amax
```

Jeff's 首刷
```python
# Runtime: 12 ms, faster than 96.86% of Python online submissions for House Robber.
# Memory Usage: 13.4 MB, less than 70.66% of Python online submissions for House Robber.
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        elif size == 1:
            return nums[0]
        
        isMaxHasLast = nums[1] > nums[0]
        (maxi, second) = (nums[1], nums[0]) if isMaxHasLast else (nums[0], nums[1])
        for i in xrange(2, size):
            if isMaxHasLast:
                if maxi >= second+nums[i]:
                    isMaxHasLast = False
                    second += nums[i]
                else:
                    tmp = maxi
                    maxi = second + nums[i]
                    second = tmp
            else:
                second = maxi
                maxi += nums[i]
                isMaxHasLast = True
        return maxi
```