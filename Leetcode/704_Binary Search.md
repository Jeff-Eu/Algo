# 704. Binary Search (Easy)
Q: Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:
```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```
Example 2:
```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
``` 

Note:

* You may assume that all elements in nums are unique.
* n will be in the range [1, 10000].
* The value of each element in nums will be in the range [-9999, 9999].

## Answer

高手速解
```python
class Solution:
    def search(self, nums, target):
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1
```

詳解的寫法 (推)

```python
# Runtime: 192 ms, faster than 88.29% of Python online submissions for Binary Search.
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            mid = (lo+hi)/2
            if nums[mid]<target:
                lo=mid+1
            elif nums[mid]>target:
                hi=mid-1
            else:
                return mid
        return -1
```
以前Jeff的寫法 (比較不好)
```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo=0
        hi=len(nums)-1
        while lo<hi:
            mid = (lo+hi)/2
            if nums[mid]<target:
                lo=mid+1
            elif nums[mid]>target:
                hi=mid
            else:
                return mid
        if nums[lo] == target:
            return lo
        else:
            return -1
```