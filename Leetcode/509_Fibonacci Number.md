# 509. Fibonacci Number
Q: The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
```
Given N, calculate F(N).

Example 1:
```
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
```
Example 2:
```
Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
```


## Answer
3刷使用 [Python 3 libary裡的cache (Python 2沒有)](https://docs.python.org/3/library/functools.html#)，但發現用在 [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) 會有 bug，還不曉得原因。

```python
# Runtime: 28 ms, faster than 85.69% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 14.4 MB, less than 9.40% of Python3 online submissions for Fibonacci Number.
from functools import cache
class Solution:
    def fib(self, n: int) -> int:
        @cache
        def fib2(n):
            if n < 2:
                return n
            return fib2(n-1) + fib2(n-2)
        
        return fib2(n)
```

Jeff's 2 刷
```python
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 2:
            return N

        f1 = 1
        f2 = 0
        
        i = 2
        while i <= N:
            out = f1 + f2
            f2 = f1
            f1 = out
            i += 1
            
        return out
```

高手解:
用memory去記前面的值是比較好的作法，好處：
1. 萬一此題變化成不限前面個數的總合，就可以用陣列來儲存，否則單純變數無法動態宣告N個
2. 這行`memo = [memo[-1], memo[-1] + memo[-2]]`的寫法，避免了我原本用f1, f2設值易犯的失誤：
    ```python
    f1 = out
    f2 = f1 # f2也變成out了 
    ```
高手解的code：
```python
class Solution(object):
    def fib(self, N):
        if N == 0: return 0
        memo = [0,1]
        for _ in range(2,N+1):
            memo = [memo[-1], memo[-1] + memo[-2]]

        return memo[-1]
```

