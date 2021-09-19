# 152. Maximum Product Subarray
Q: Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```
Example 2:
```
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

# 思路
maxHere 代表到index i 可得到的maximum product.
minHere 代表到index i 可得到的minimum product.

# Answer
高手解
```python
class Solution(object):
    # 高手解
    def maxProduct(self, A):
        r = A[0]
        imax = imin = r
        for i in xrange(1, len(A)):
            
            if A[i] < 0:
                # multiplied by a negative makes big number smaller, small number bigger
                # so we redefine the extremums by swapping them
                imax, imin = imin, imax
                
            # 數學: 
            # 1. 若 c<0 且 a>b 則 ac < bc ；若 c>0 則 ac > bc
            # 2. 承上 a > b > c > d (a最大d最小) 且 s<0 則 as < bs < cs < ds (ds最大as最小)
            imax = max(A[i], imax * A[i])
            imin = min(A[i], imin * A[i])
            
            r = max(r, imax)
        return r
```

同上，只是稍微好理解一點
```python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=nums[0]
        imin = imax = r
        for i in xrange(1, len(nums)):

            if nums[i]<0:
                tmpImax= imax # 避免在求 imin時使用到被修改過的imax，故先將它暫存
                # 數學: 
                # 1. 若 c<0 且 a>b 則 ac < bc ；若 c>0 則 ac > bc
                # 2. 承上 a > b > c > d (a最大d最小) 且 s<0 則 as < bs < cs < ds (ds最大as最小)
                imax=max(nums[i], imin*nums[i])
                imin=min(nums[i], tmpImax*nums[i])
            else:
                imax=max(nums[i], imax*nums[i])
                imin=min(nums[i], imin*nums[i])

            r=max(r,imax)
            
        return r
```

## Approach #1 Dynamic Programming [Accepted]
```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    var length = nums.length;
    var maxPre = nums[0];
    var minPre = nums[0];
    var maxSofar = nums[0];
    var maxHere;
    var minHere;
    
    for (var i = 1; i < length; i++) {
        maxHere = Math.max(Math.max(nums[i] * maxPre, nums[i] * minPre), nums[i]);
        minHere = Math.min(Math.min(nums[i] * maxPre, nums[i] * minPre), nums[i]);
        maxSofar = Math.max(maxSofar, maxHere);
        maxPre = maxHere;
        minPre = minHere;
    }
    return maxSofar;
};
```