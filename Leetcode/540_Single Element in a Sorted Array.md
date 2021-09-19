# 540. Single Element in a Sorted Array 
Q: You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:
```
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
```
Example 2:
```
Input: nums = [3,3,7,7,10,11,11]
Output: 10
```

Constraints:

* 1 <= nums.length <= 10^5
* 0 <= nums[i] <= 10^5

## Answer
[stephan高手解](https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/100732/Short-compare-numsi-with-numsi1):
```python
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums)-1
        
        while lo<hi:
            mid = (lo+hi)/2
            # print mid
            if nums[mid] == nums[mid^1]:
                lo = mid+1
            else:
                hi = mid
                
        return nums[hi] # lo == hi
```

學平簡單快速解:

每次往前移動兩個元素，看是不是跟前一個相同，若不相同就是只有一個元素發生的位置