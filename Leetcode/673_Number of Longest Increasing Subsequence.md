# 673. Number of Longest Increasing Subsequence
Q: Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

Example 1:
```
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
```
Example 2:
```
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
```
## Answer
寫這題的時候有想到用額外一個陣列去存次數，但是又想走捷徑用一個變數去累積次數就好，最後發現只用一個變數似乎做不出來，然後看了一下論譠也有人用額外一個陣列去存次數，因此對最初的構想有了信心，就在沒有看他的code情況下寫出來了(而且那時候是下午剛睡醒有一點醉的時候)

外記: 推文有人覺得這題是hard，當然沒寫過第300題一定覺得是 hard，但寫過就覺得是 medium (看來真的要從數字少的開始寫呀！)

Jeff's (60分)
```python
# Runtime: 976 ms, faster than 73.04% of Python online submissions for Number of Longest Increasing Subsequence.

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        
        dp = [0]*size
        arr=[0]*size
        amax=0
        out=0
        for i in xrange(size):
            lmax=0
            arr[i]=1
            for j in xrange(i):
                if nums[j]<nums[i]:
                    if dp[j]>lmax:
                        arr[i]=arr[j]
                        lmax=dp[j]
                    elif dp[j]==lmax:
                        arr[i]+=arr[j]
                        
            dp[i]=lmax+1
            
            amax=max(amax, dp[i])
        
        for i in xrange(size):
            if dp[i]==amax:
                out+=arr[i]
        
        return out
```