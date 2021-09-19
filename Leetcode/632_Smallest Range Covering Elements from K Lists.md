# 632. Smallest Range Covering Elements from K Lists
Q: You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

Example 1:
```
Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
```
Example 2:
```
Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
```
Example 3:
```
Input: nums = [[10,10],[11,11]]
Output: [10,11]
```
Example 4:
```
Input: nums = [[10],[11]]
Output: [10,11]
```
Example 5:
```
Input: nums = [[1],[2],[3],[4],[5],[6],[7]]
Output: [1,7]
```
## Answer

這題跟 76 很像，也是容易出錯的一題，但不像 76 可以再用 queue 去做最佳化，所以測驗時統一將 window left 一次向右移動一格就好，比較好寫。

Time估計： O(N*logN) + O(N) = O(N*logN), N is total number in nums
```python
# Runtime: 200 ms, faster than 94.37% of Python online submissions for Smallest Range Covering Elements from K Lists.
# Memory Usage: 21.6 MB, less than 16.90% of Python online submissions for Smallest Range Covering Elements from K Lists.
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        size = len(nums)
        ls = []
        for i in xrange(size):
            for v in nums[i]: # !) 寫錯成 v in xrange(len(nums[i])):
                ls.append((v, i))
                
        ls.sort()
        l = r = 0
        sizels = len(ls)
        mp = {}
        for i in xrange(size):
            mp[i] = 0
        toGoal = 0
        out = (float("inf"), 0, 0)
        while r < sizels:
            
            pair = ls[r]
            mp[pair[1]] += 1
            if mp[pair[1]] == 1:
                toGoal += 1
                
            while toGoal == size and l<=r:
                
                length = ls[r][0]-ls[l][0]  # !) 把 ls寫錯成 pair
                if length < out[0]:
                    out = (length, ls[l][0], ls[r][0])
                    
                lpair = ls[l]
                mp[lpair[1]] -= 1
                if mp[lpair[1]] == 0:
                    toGoal -= 1
                l+=1

            r += 1
        
        return [out[1], out[2]]
'''reason:
[ 4, 10,15,  24,26],
[0, 9,12, 20],
[  5,    18,22,   30]

0 4 5 9 10 12 15 18 20 22 24 26
1 0 2 1  0  1  0  2  1  2  0  0
'''
```