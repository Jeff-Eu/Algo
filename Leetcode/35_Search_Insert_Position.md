# 35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

## 思路
* 運用 binary search 去尋找 target 的 index

## Answer
二刷:
* 新技能：Binary search 的 boundary case問題可以將test data縮小至只有兩個元素的情況，再來微調程式。

```python
# Runtime: 28 ms, faster than 96.14% of Python online submissions for Search Insert Position.
# Memory Usage: 14.2 MB, less than 28.04% of Python online submissions for Search Insert Position.
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        
        lo = 0
        hi = size-1
        
        if target > nums[hi]:
            return size
        
        while lo < hi:
            mid = (lo+hi)/2
            
            if nums[mid] < target:
                lo = mid+1
            elif nums[mid] > target:
                hi = mid
            else: # nums[mid] == target
                return mid
            
        return lo
```

Jeff's
```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        right = len(nums)- 1 
        left = 0
        
        while right >= left:
            mid = (left+right)/2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        if right < 0:
            return 0
        elif left == len(nums):
            return left
        
        return left
```

學平's
```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    var left = 0;
    var right = nums.length;
    var mid;
    
    while(left < right) {
        mid = left + parseInt((right - left)/2); 
        if (target > nums[mid]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    return left;
};
```