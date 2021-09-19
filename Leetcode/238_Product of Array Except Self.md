# 238. Product of Array Except Self
Q: Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
```
Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
```
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

## Answer
詳解有兩段進化解法，看完第一段解後有寫出首刷，但沒有比詳解的好，不過意外發現我的解法中有一段code可以做成一個 easy等級的題目。

實戰中要先寫出第一段解，再做出第二段比較合理。

二刷(類似詳解二。寫出第一段解後再花約25分):
```python
# Runtime: 236 ms, faster than 81.73% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21.3 MB, less than 53.83% of Python3 online submissions for Product of Array Except Self.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        right = [1]*size
            
        for i in range(size-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
            
        c = 1
        for i in range(1, size):
            c *= nums[i-1]
            right[i] *= c
            
        return right
'''reasoning
r: 24 12 4 1
l: 1 1 2 6

24 12 8 6
'''
```

## Archived
首刷(不推):
```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        
        R = [0]*length

        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]
        
        # 下面這小段可以變成一個easy等級的題目 => Q: 如何獲得 left product array with O(N) time and O(1) space ?
        last = nums[0]
        nums[0] = 1
        for i in range(1, length):
            tmp = nums[i]
            nums[i] = last * nums[i-1]
            last = tmp
            
        
        R[0] = R[0] * nums[0]
        for i in range(1, length):
            R[i] = R[i] * nums[i]
        
        return R
```

詳解的第一段解(要看它的動畫才比較清楚):
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array 
        length = len(nums)
        
        # The left and right arrays as described in the algorithm
        L, R, answer = [0]*length, [0]*length, [0]*length
        
        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the L[0] would be 1
        L[0] = 1
        for i in range(1, length):
            
            # L[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1]
        
        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R[length - 1] would be 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            
            # R[i + 1] already contains the product of elements to the right of 'i + 1'
            # Simply multiplying it with nums[i + 1] would give the product of all 
            # elements to the right of index 'i'
            R[i] = nums[i + 1] * R[i + 1]
        
        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i]
        
        return answer
```

詳解的第二段解
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array 
        length = len(nums)
        
        # The answer array to be returned
        answer = [0]*length
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1;
        for i in reversed(range(length)):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
```