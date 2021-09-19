# 40. Combination Sum II
Q: Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

* All numbers (including target) will be positive integers.
* The solution set must not contain duplicate combinations.

Example 1:
```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```
Example 2:
```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

Answer:

Jeff's first solution (beat 72%)
```python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        nums = candidates
        res = []
        self.dfs(nums, 0, target, [], res)
        # res = list(set(res))
        return res
        
    def dfs(self, nums, index, target, path, res):
        if target < 0:
            return
        elif target == 0:
            if path not in res:
                res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, target-nums[i], path + [nums[i]], res)
            if target-nums[i] <= 0:
                break
```

Best solution (beat 100%). Original is from [here](https://leetcode.com/problems/combination-sum-ii/discuss/16944/Beating-98-Python-solution-using-recursion-with-comments).

```python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(candidates, 0, target, [], res)
        return res
        
    def dfs(self, nums, index, target, path, res):

        # 下面兩行亦可省略
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
            
        for i in xrange(index, len(nums)):
            
            # 注意這兩行雖然跟 Three sum過濾重覆的概念類似，但有點變化 
            if i>index and nums[i] == nums[i-1]:
                continue

            if target-nums[i] < 0:
                break
                
            # 透過dfs深度呼叫時，是"新增結點"；反之透過前面for迴圈跑是"移動結點"，
            # 每次發生重覆組合的時機點是在"移動"到重覆數字的結點才會發生重覆組合，
            # 因此前面才要有
            # if i>index and nums[i] == nums[i-1]: 的判斷
            self.dfs(nums, i+1, target-nums[i], path + [nums[i]], res)
```

簡化上面的寫法如下(實戰採用):
```python
# Runtime: 28 ms, faster than 96.39% of Python online submissions for Combination Sum II.
# Memory Usage: 13.4 MB, less than 62.70% of Python online submissions for Combination Sum II.
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(index, target, path):
            
            if target == 0:
                res.append(path)
                return

            for i in xrange(index, len(nums)):
                # 注意這兩行跟 90. Subsets II 過濾重覆的寫法一樣；類似方法也用在 15. Three Sum
                if i>index and nums[i] == nums[i-1]:
                    continue

                if target-nums[i] < 0:
                    break

                dfs(i+1, target-nums[i], path + [nums[i]])
            
        candidates.sort()
        nums = candidates # simplify name
        res = []
        dfs(0, target, [])
        return res
```