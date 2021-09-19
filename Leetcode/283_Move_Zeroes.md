# 283. Move Zeroes
Q: Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```
Note:

1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.

## Answer
Jeff 首刷 (14:26)

這種題目最好都先用打字的打出幾個範例input來協助思考出有創造力的解法

1. Find the index p which points to the left most zero.
2. Check each element from left most to right most. If the element is NOT zero, swap the element and the one which p points to. Then move p forward ONE index.
    ```
    40000319  
     p   i

    =>

    43000019
      p  i
    ``` 
3. Repeat the step 2.
```python
# Runtime: 40 ms, faster than 44.24% of Python online submissions for Move Zeroes.
# Memory Usage: 14.4 MB, less than 49.59% of Python online submissions for Move Zeroes.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        p = -1 # pointer
        for i in xrange(N):
            if p == -1 and nums[i] == 0:
                p = i
            elif p != -1 and nums[i] != 0:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
```

Jeff 2刷(看過自己的詳解後):
改良一刷，i從p+1開始跑
```python
# Runtime: 36 ms, faster than 69.42% of Python online submissions for Move Zeroes.
# Memory Usage: 14.4 MB, less than 73.81% of Python online submissions for Move Zeroes.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        p=size # 也可以設為-1比較好理解，但第二個迴圈就要先判斷p是否不為-1了
        for i in xrange(size):
            if nums[i]==0:
                p=i
                break

        for i in xrange(p+1, size): # start from p+1 because p must be zero
            if nums[i] != 0:
                nums[i], nums[p] = nums[p], nums[i]
                p+=1
                continue
```