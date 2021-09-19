# 494. Target Sum
Q: You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
```
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
```

## Answer
一開始馬上想出暴力解，但懶得寫，也想不出來。 後來想到高人說先寫暴力解再來想有無最佳解，所以就花了約十分鐘把暴力解寫出，後來觀察code真的發現有dp可以改善，就再花了9分鐘把最佳解寫出來了。

注意這邊時間複雜度的計算可以從 hsh 的個數來觀察，就能避開遞迴計算時間複雜度。

新技能: 
* memoization 方法若需要在2維上用，可以用 dictionary 來取代二維陣列會方便許多，dictionary可以比二維陣列小，而且又不會像二維陣列初始化那麼麻煩；但如果是bottom-up的 2維DP，就不建議用dictionary，因為 `dp(i, j)` 可能會存取到還沒被初始化過的值，那用先初始化過的二維陣列會比較安全。
* sum 可以取名叫 sm
* dictionary/2D dp array 可以取名叫 mp (map)

經驗:
* 以後若5分鐘內想不到最佳解，就先用暴力解寫出再想有無改善成最佳解的機會。
* 像這題有遞迴又有DP解，那時間複雜度計算可以從 dp 的個數來觀察，就能避開遞迴計算時間複雜度的麻煩。

Time: O(n*l)  n是nums個數， l是所有和的組合，會介於 +/-sum(|q| for q in nums)
```python
# Runtime: 376 ms, faster than 57.86% of Python online submissions for Target Sum.
# Memory Usage: 43.2 MB, less than 5.36% of Python online submissions for Target Sum.
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        size = len(nums)
        mp = {}
        def dfs(idx, sm):
            if idx==size:
                if sm==S:
                    return 1
                return 0
            
            if (idx, sm) in mp:
                return mp[(idx, sm)]
            
            out1 = dfs(idx+1, nums[idx]+sm)
            out2 = dfs(idx+1, -nums[idx]+sm)
            mp[(idx, sm)] = out1+out2
            return out1+out2
            
        return dfs(0, 0)
'''
[2, 1, 1] 

sum(|q| for q in nums) 
< S => 0
> S => ?

sum(-|q| for q in nums) 
> S => 0
< S => ?

4 2 -1 5
'''
```