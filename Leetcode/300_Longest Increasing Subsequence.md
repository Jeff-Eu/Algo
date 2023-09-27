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

解答:

Solution 1: Dynamic Programming

This is a classic Dynamic Programming problem.
Let dp[i] is the longest increase subsequence (LIS) of nums[0..i] which has nums[i] as the end element of the subsequence.

注意，上面的陳述，並非代表 dp[i] 就是 nums[0..i] 中的 LIS，因為有可能存在的 LIS 並非是以 nums[i] 作為 subsequence的結尾；所以下面的源碼才會回傳 max(dp)，而非 dp[-1]

就算有上面提示，直接看code還是不易理解它的做法，先看看下面這影片教學，大概看不到一半就能理解並自己實作了
https://www.youtube.com/watch?v=fV-TF4OvZpk&t=1s

```python 3
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
            
        sz = len(nums)
        dp = [1]*sz
        for i in range(1, sz):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
```


舊刷記錄:

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

## Relation
- 進階: [[673_Number of Longest Increasing Subsequence]]
