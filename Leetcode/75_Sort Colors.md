# 75. Sort Colors
Q: Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
 

Example 1:
```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```
Example 2:
```
Input: nums = [2,0,1]
Output: [0,1,2]
```
Example 3:
```
Input: nums = [0]
Output: [0]
```
Example 4:
```
Input: nums = [1]
Output: [1]
```

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.

## Answer
https://leetcode-cn.com/problems/sort-colors/solution/yan-se-fen-lei-by-leetcode-solution/
* 面試時可先寫一個指標，再寫兩個指標(較難)

* 兩個指標的解法
```python
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """ 
        p=q=0
        for i in xrange(len(nums)):
            if nums[i]==0:
                nums[i], nums[p]=nums[p], nums[i]
                if p<q:
                    nums[i],nums[q]=nums[q],nums[i]
                p+=1
                q+=1
            elif nums[i]==1:
                nums[i], nums[q]=nums[q], nums[i]
                q+=1
        return nums
```
