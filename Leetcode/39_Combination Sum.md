# 39. Combination Sum
Q: Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

* All numbers (including target) will be positive integers.
* The solution set must not contain duplicate combinations.

Example 1:
```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```
Example 2:
```
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

## Answer
Jeff 最精簡解，列舉到不能再列舉為止。
```python
# Runtime: 72 ms, faster than 68.77% of Python online submissions for Combination Sum.
# Memory Usage: 13.3 MB, less than 87.75% of Python online submissions for Combination Sum.
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = candidates # short name
        def dfs(target, path, idx):
            if target == 0:
                r.append(path)
            elif target > 0:
                for i in xrange(idx, len(nums)):
                    dfs(target-nums[i], path+[nums[i]], i)
        r = []
        dfs(target, [], 0)
        return r
```

從上面的解的加速版：先由小到大排序，就可以從`if target-nums[i] <= 0:`這判斷式去濾掉不必要的計算:
```python
# Runtime: 44 ms, faster than 88.87% of Python online submissions for Combination Sum.
# Memory Usage: 13.3 MB, less than 87.75% of Python online submissions for Combination Sum.
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort() # compulsory
        nums = candidates # shorten name
        def dfs(target, path, idx):
            if target == 0:
                r.append(path)
            elif target > 0:
                for i in xrange(idx, len(nums)):
                    dfs(target-nums[i], path+[nums[i]], i)
                    if target-nums[i] <= 0:
                        break
        r = []
        dfs(target, [], 0)
        return r
```

## Archive when I'm a novice

從原始答案改進可讀性後的寫法
```python
class Solution(object):
    def __init__(self):
        
      self.nums = []
      self.res = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.nums = candidates
        # self.nums.sort()
        self.dfs(target, 0, [])
        return self.res

    def dfs(self, target, index, path):
        if target < 0:
            return  # backtracking
        if target == 0:
            self.res.append(path)
            return
        for i in xrange(index, len(self.nums)):
            self.dfs(target-self.nums[i], i, path+[self.nums[i]])
```    

下面為原始答案加速後的改進版(60% -> 98%)，我上面的寫法只是化簡少了dfs函式的兩個參數，將他們移至fields中，但上面寫法速度會變慢，可能跟fields的建立有關

其他觀念：
* 寫Leetcode時不要用static 變數存List，特別是答案，否則它可能會在每次跑不同test時將答案都累加上去
* 感覺初始有fields的物件跑起來會比較慢，所以建議還是傳值給function，要練習這種寫法；不要寫fields
* Q: why sorting before doing dfs ?
	 A: Yes, sorting is not for correctness but for speed. What we do by sorting is we limit the range of numbers on which we call dfs recursively, as we know the numbers outside the range cannot be in our solution. For small inputs this speed up may not be substantial but for larger inputs, sorting will definitely give you faster solution. 


```python
class Solution(object):
    def combinationSum(self, candidates, target):
    #     """
    #     :type candidates: List[int]
    #     :type target: int
    #     :rtype: List[List[int]]
    #     """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in xrange(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
            # if前面有sort，下面兩行是我想到能再用葉結點過濾不必要的traverse，不加打敗60%，加了打敗98%
            if target-nums[i] <= 0:
                break
```