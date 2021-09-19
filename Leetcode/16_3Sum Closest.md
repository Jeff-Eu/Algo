# 16. 3Sum Closest
Q: Given an array `nums` of n integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

**Example 1:**

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

**Constraints:**
* 3 <= nums.length <= 10^3
* -10^3 <= nums[i] <= 10^3
* -10^4 <= target <= 10^4

## Answer
這題跟第15題3Sum 很像，基本上會寫第15題這題就能解出。

解一，考慮重覆的組合(較慢，較簡潔)
```python
# Runtime: 96 ms, faster than 68.79% of Python online submissions for 3Sum Closest.
# Memory Usage: 13.5 MB, less than 51.91% of Python online submissions for 3Sum Closest.
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = float("inf")
        size = len(nums)
        for i in xrange(size-2):
            j = i+1
            k = size-1
            
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                if abs(s-target) < abs(diff):
                    diff = s-target
                    
                if s > target:
                    k-=1
                elif s < target:
                    j+=1
                else: # s == target:
                    return target
                
        return diff + target
```

二刷約25分，忽略重覆的組合(較快，稍複雜但必會)
```python
# Runtime: 104 ms, faster than 92.78% of Python3 online submissions for 3Sum Closest.
# Memory Usage: 14.1 MB, less than 97.92% of Python3 online submissions for 3Sum Closest.
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        size = len(nums)
        mindiff = float("inf")
        minsum = 0
        for i in range(size-2):
            if i>0 and nums[i]==nums[i-1]:
                continue

            j = i+1
            k = size-1
            while j<k:
                sm = nums[i]+nums[j]+nums[k]
                if sm > target:
                    if abs(mindiff) > abs(sm-target):
                        mindiff = sm-target
                        minsum = sm
                    
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    k-=1
                elif sm < target:
                    if abs(mindiff) > abs(sm-target):  # 下面這幾行重覆了，可以合併至外面一層，簡化程式 
                        mindiff = sm-target
                        minsum = sm
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    j+=1
                else:
                    return target
                
        return minsum
```