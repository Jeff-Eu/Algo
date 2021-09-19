# 448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

**Example:**

```
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
```

### Answer

首刷: 約18分

這題有用過類似的觀念就很容易解出，其實這類題目都滿有意思的，有應用價值。

```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sz = len(nums)
        for i in xrange(sz):
            idx = abs(nums[i])-1
            if nums[idx] > 0:
                nums[idx] *= -1
                
        ans = []
        for i in xrange(sz):
            if nums[i] > 0:
                ans.append(i+1)
                
        return ans
```