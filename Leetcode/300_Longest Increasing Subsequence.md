# 300. Longest Increasing Subsequence
Q: Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 
Example 1:
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```
Example 2:
```
Input: nums = [0,1,0,3,2,3]
Output: 4
```
Example 3:
```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up:

* Could you come up with the O(n2) solution?
* Could you improve it to O(n log(n)) time complexity?

* 進階題：673. Number of Longest Increasing Subsequence

## Answer
還有binary search結合DP的最佳解方法還沒理解

以下是單純DP解
dp[i] represents the length of the longest increasing subsequence on an array from index 0 to i, ALSO ! the subsequence must end with index i.

```python
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        size = len(nums)
        dp=[0]*size
        amax=0
        
        for i in xrange(size):

            lmax=0
            for j in xrange(i):
                if nums[i]>nums[j]:
                    lmax=max(lmax, dp[j])
            dp[i] = lmax+1
            amax=max(amax, dp[i]) # This must be included ! Can't only return dp[-1] as answer 
            
        return amax  
```
