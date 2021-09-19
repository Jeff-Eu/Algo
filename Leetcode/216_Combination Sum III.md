# 216. Combination Sum III
Q: Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:
```
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
```
Example 2:
```
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
```
Example 3:
```
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.
```
Example 4:
```
Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.
```
Example 5:
```
Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
​​​​​​​There are no other valid combinations.
```
## Answer
2021/1/31 整理出排列組合問題後 10分寫出
```python
# Runtime: 20 ms, faster than 72.63% of Python online submissions for Combination Sum III.
# Memory Usage: 13.5 MB, less than 13.91% of Python online submissions for Combination Sum III.
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(idx, pick, summ, arr):
            if pick==k and summ==n:
                ans.append(arr)
                return
                
            for i in xrange(idx, size):
                dfs(i+1, pick+1, summ + nums[i], arr+[nums[i]])
            
        ans=[]
        nums=xrange(1, 10)
        size = len(nums)
        dfs(0, 0, 0, [])
        return ans
```