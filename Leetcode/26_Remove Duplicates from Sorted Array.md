# 26. Remove Duplicates from Sorted Array
Q: Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
```
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
```
Example 2:
```
Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:
```
Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.\
// using the length returned by your function, it prints the first len elements.
```
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```
## Answer
Jeff 覆刷, 下面是比較單純的方法。其他還有想到的方法是用一個變數指向目前該更新的位置index，另外再用一個變數暫存目前最近更新過的數值，用來判斷避免跟它重覆。
```python 3
'''
Input: nums = [0,0,1,1,1,2,2,3,3,4]
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        arr = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                arr.append(nums[i])

        k = len(arr)
        for i in range(k):
            nums[i] = arr[i]

        return k
```


Jeff's
```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        i = len(nums) - 1
        last = nums[i]
        i -= 1
        while i >= 0:
            if nums[i] == last:
                nums.pop(i)
            else:
                last = nums[i]
            i -= 1
            
        return len(nums)
```