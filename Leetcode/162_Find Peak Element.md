# 162. Find Peak Element
Q: A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```
Example 2:
```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```
## Answer
這題非常簡單，不知為何難度為medium，但要小心boundary case，考的是細心程度。

注意 java 不像 python，在取 size 時，字串，ArrayList, 還有 Array 的方法都不一樣XD。

python
```python
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        
        pre = -float("inf")
        for i in xrange(size):
            if nums[i] < pre:
                return i-1
            else:
                pre = nums[i]
                
        return size-1
```

java
```java
class Solution {
    public int findPeakElement(int[] nums) {
        
        int size = nums.length;
        
        long pre = Long.MIN_VALUE;
        for(int i=0; i<size; i++) {
            if(nums[i] > pre)
                pre = nums[i];
            else
                return i-1;
        }
        return size-1;
    }
}
```