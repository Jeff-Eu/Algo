# 31. Next Permutation
Q: Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
```
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
```

## Answer
這題在Leetcode有詳解，主要是這兩張圖的解釋
![img1](imgs/31_nums_graph.png)
![img2](imgs/31_Next_Permutation.gif)

Jeff's (看過解答後)
```python
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        
        def swapsort(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -=1

        for i in xrange(size-1, 0, -1):
            print i
            if nums[i] > nums[i-1]:
                tmpi = i
                for j in xrange(i, size):
                    if nums[j] > nums[i-1]: # Note the boundary case here, j == size-1, so we set tmpi = j every time 
                        tmpi = j
                nums[i-1], nums[tmpi] = nums[tmpi], nums[i-1]
                left = i
                right = size - 1
                swapsort(left, right)
                
                return nums
        
        return swapsort(0, size-1)
```