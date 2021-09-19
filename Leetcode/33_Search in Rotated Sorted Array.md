# 33. Search in Rotated Sorted Array
Q: You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

 

Example 1:
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```
Example 2:
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```
Example 3:
```
Input: nums = [1], target = 0
Output: -1
``` 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4

## Answer
這題算是 153. Find Minimum in Rotated Sorted Array的進階題，這題會reuse到 153題的解！

研究出Binary Search的理論後(見1011題的分析)首刷，使用 Upper Bound BS：
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
                
        def BS(L, R):
            lo = L
            hi = R
            
            while lo<=hi:
                mid = (lo+hi)//2
                if nums[mid] > target:
                    hi = mid-1
                elif nums[mid] < target:
                    lo = mid+1
                else:
                    return mid
            return -1
            
        lo = 0
        hi = len(nums)

        # 下面先來取最大值...

        # Compulsory: 排除正常Array
        '''
        注意為何需要排除沒被rotate過的正常array，因為這時取的mid當hi，並不會讓max落在lo跟hi之間，產生矛盾；但若是求min (Leetcode 153)，無論什麼情形，lo/hi的移動都不會發生這種矛質，因此不需做這種排除動作。  Cheat Sheet: 因此以後遇到 Rotation Array的問題，都先求 Min！
        '''
        if nums[-1] >= nums[0]:
            # do usual binary search
            return BS(lo, hi-1)
        
        # Use upper bound BS to find the index of the largest value
        lastIdx = hi-1
        while lo<hi:
            mid = (lo+hi)//2
            if nums[mid]<=nums[lastIdx]:
                hi = mid
                lastIdx = hi
            else:
                lo = mid + 1
                
        maxIdx = hi-1
        # print (maxIdx)
        if nums[0] <= target:
            return BS(0, maxIdx)
        else:
            return BS(maxIdx+1, len(nums)-1)
```

## Archived
[參考了更好的高手解後Jeff的第一刷](https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution):

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
        
        imin=0 # First, find the min index inside the array (No.153 problem)
        if nums[hi]>nums[lo]:
            imin=lo
        else:
            while lo<hi:
                mid=(lo+hi)/2
                if nums[mid]<nums[0]:
                    hi=mid
                else:
                    lo=mid+1
            imin=lo
        
        if target==nums[0]:
            return 0
        
        if target>nums[0]:
            lo=0
            hi=len(nums)-1 if imin==0 else imin-1
        else:
            lo=imin
            hi=len(nums)-1
            
        # Common binary search
        while lo<hi:
            mid=(lo+hi)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                hi=mid
            else:
                lo=mid+1

        if nums[lo]==target:
            return lo
        else:
            return -1
```

難懂的高手解法by Stephan:
[Stephan的解釋](https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple)
```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) # for lo < hi, so not using size-1
        
        while lo < hi:
            mid = (lo+hi)/2
            n = nums[mid] if (target >= nums[0]) == (nums[mid] >= nums[0]) else float("inf") if (nums[0]<=target) else -float("inf")      # note that the "equal" case is compulsory, try to think it

            if n < target:
                lo = mid+1
            elif n > target:
                hi = mid
            else:
                return mid
        return -1
```
