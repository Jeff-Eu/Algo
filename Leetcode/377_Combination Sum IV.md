# 377. Combination Sum IV
Q: Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:
```
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
```
Note that different sequences are counted as different combinations.

Therefore the output is 7.
 
Follow up:
* What if negative numbers are allowed in the given array?
* How does it change the problem?
* What limitation we need to add to the question to allow negative numbers?

## Answer
2021/2/28 二刷，先在25分內寫出 Memoization，後來又再約22分鐘想出並寫出 DP解！

發現畫圖沒幫助想到dp解，但一開始先用列舉法寫出之後就容易改成memoization解，之後用註解推理的方式較容易想到 DP 解。

Top-Down Meomoization Approach
```python
# Runtime: 788 ms, faster than 5.49% of Python3 online submissions for Combination Sum IV.
# Memory Usage: 25.5 MB, less than 5.17% of Python3 online submissions for Combination Sum IV.
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        size = len(nums)
        mp = {}
        def dfs(idx, sm):
            if sm == target:
                mp[(idx, sm)] = 1
                return 1
            elif sm > target:
                mp[(idx, sm)] = 0
                return 0
            
            if (idx, sm) in mp:
                return mp[(idx, sm)]
            
            c = 0
            for i in range(size):
                c += dfs(i, nums[i] + sm)
            mp[(idx, sm)] = c
            return c
        
        return dfs(0, 0)
```

Bottom-up DP Approach
```python
# Runtime: 44 ms, faster than 73.07% of Python3 online submissions for Combination Sum IV.
# Memory Usage: 14.7 MB, less than 46.72% of Python3 online submissions for Combination Sum IV.        
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        size = len(nums)
        # bottom up approach
        
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1, target+1): # 小心若從0就錯了
            dp[i] = sum(dp[i-v] for v in nums if i-v>=0)
            
        return dp[target]
'''
dp[ta] = dp[ta-3] + dp[ta-2] + dp[ta-1]
dp[i] = sum(dp[i-v] for v in nums)
'''
```

## Archived
這題不能用列舉的方式解，會超時，把樹狀圖畫出來，是可能會觀察到有重覆計算之處，但對想出DP幫助不大，還是用註解推理較好。

[力扣高手有很詳細的解說](https://leetcode-cn.com/problems/combination-sum-iv/solution/dong-tai-gui-hua-python-dai-ma-by-liweiwei1419/)

[另外還有一個力扣鄉民做的解題技巧整理，要等其他題都做過才比較容易懂](https://leetcode-cn.com/problems/combination-sum-iv/solution/xi-wang-yong-yi-chong-gui-lu-gao-ding-bei-bao-wen-/)

```python
# Runtime: 24 ms, faster than 98.23% of Python online submissions for Combination Sum IV.
# Memory Usage: 13.6 MB, less than 98.82% of Python online submissions for Combination Sum IV.
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0]*(target+1)
        dp[0] = 1
        for i in xrange(1, target+1):
            for n in nums:
                if i >= n:
                    dp[i] += dp[i-n]
                    
        return dp[target]
        
# 下面為列舉的寫法，只能用在列舉集合，否則像這題只求數字就可能存在DP解，用列舉的寫法會超時
#         def perm(ls):
            
#             def dfs2(ls2):
#                 if not ls2:
#                     ans[0] += 1
                
#                 st = set()
#                 size2 = len(ls2)
#                 for i in xrange(size2):
#                     if ls2[i] in st:
#                         continue
#                     v = ls2.pop(i)
#                     st.add(v)
#                     perm(ls2)
#                     ls2.insert(i,v)             
            
#             dfs2(ls)
        
        
#         nums.sort()
#         def dfs(idx, summ, ls):
#             if summ >= target:
#                 if summ == target:
#                     perm(ls)
#                 return
                
#             for i in xrange(idx, size):
#                 dfs(i, summ + nums[i], ls+[nums[i]])
            
#         ans = [0]
#         size = len(nums)
#         dfs(0, 0, [])
#         return ans[0]
```