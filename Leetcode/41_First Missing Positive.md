# 41. First Missing Positive
Q: Given an unsorted integer array nums, find the smallest missing positive integer.

Example 1:
```
Input: nums = [1,2,0]
Output: 3
```
Example 2:
```
Input: nums = [3,4,-1,1]
Output: 2
```
Example 3:
```
Input: nums = [7,8,9,11,12]
Output: 1
```
## Answer
15初解，45分較佳解

一開始看不懂題目，卡了幾分鐘

* 一樣先寫可行的解法，再慢慢最佳化
* 記得用個note做理解推理才不會出差錯

Time: O(n) n is len(nums)
Space: O(1)
```python
# Runtime: 20 ms, faster than 84.62% of Python online submissions for First Missing Positive.
# Memory Usage: 13.4 MB, less than 88.19% of Python online submissions for First Missing Positive.
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
# Heap Approach
        heapq.heapify(nums)
        
        i = 1
        while True:
            if not nums:
                return i
            
            if i > nums[0]:
                heapq.heappop(nums)
            elif i == nums[0]:
                heapq.heappop(nums)
                i+=1                
            else:
                return i
                                
        return -1
'''reasoning
n: 0 1 2

i: 1 2 3
'''   
# # Hash Approach (First approach)
# Runtime: 20 ms, faster than 84.62% of Python online submissions for First Missing Positive.
# Memory Usage: 13.5 MB, less than 66.69% of Python online submissions for First Missing Positive.
#         st = set()
#         for n in nums:
#             st.add(n)
            
#         i = 0
#         while True:
#             i+=1
#             if i in st:
#                 continue
#             else:
#                 return i
#         return -1
'''
1 2 3 ....

nums [1, 2, 0]
'''
```