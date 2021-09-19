# 34. Find First and Last Position of Element in Sorted Array
Q: Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 
Example 1:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```
Example 2:
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```
Example 3:
```
Input: nums = [], target = 0
Output: [-1,-1]
``` 

Constraints:
* 0 <= nums.length <= 105
* -109 <= nums[i] <= 109
* nums is a non-decreasing array.
* -109 <= target <= 109

## Answer
前置題是 704 題，用標準解解出後，這題才比較有機會快速漂亮的解出來
```python
# Runtime: 56 ms, faster than 98.46% of Python online submissions for Find First and Last Position of Element in Sorted Array.
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        
        def bisect(lo, hi):
            
            while lo<=hi:
                mid = (lo+hi)/2
                if nums[mid]<target:
                    lo=mid+1
                elif nums[mid]>target:
                    hi=mid-1
                else:
                    return (lo, hi, mid)
            return None
            
        def findStart(lo, hi):
            ans = bisect(lo, hi)
            if not ans:
                return -1
            
            tmp = None
            while ans:
                tmp = ans
                ans = bisect(0, ans[2]-1)
                
            return tmp[2]
        
        def findEnd(lo, hi):
            
            ans = bisect(lo, hi)
            if not ans:
                return -1
            
            tmp = None
            while ans:
                tmp = ans
                ans = bisect(ans[2]+1, size-1)
            
            return tmp[2]
                
        s = findStart(0, size-1)
        e = findEnd(0, size-1)
        return [s, e]
```