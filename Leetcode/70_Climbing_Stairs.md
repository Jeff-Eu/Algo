# 70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```
Example 2:
```
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```
## Ans
複刷 - DP

解釋:
* 倒數第二個元素的英文 - second-to-last element
* 先解釋dp公式再解釋程式是保險牌
* 因為我用的dp陣列不是儲存從 1~n 的全部資料，而是只存兩個元素，這會在解釋上相對較困難
    `ways of k steps = (ways of k-1 steps) + (ways of k-2 steps)`
```python 3
class Solution:
    def climbStairs(self, n: int) -> int:
        
        arr = [0, 1, 1]

        for i in range(2, n+1):
            arr = [arr[-1], arr[-1]+arr[-2]]

        return arr[-1]
```

jeff's
```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # k3 = k1 + k2
        # ki = k(i-1) + k(i-2)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        n1 = 2
        n2 = 1
        
        for i in xrange(3, n+1):
            tmp = n1
            n1 = n1 + n2
            n2 = tmp
            
        return n1
```

學平's

## Approach #1 Brute Force [Time Limit Exceeded]
climbStairs(i, n) = climbStairs(i + 1, n) + climbStairs(i + 2, n), i 代表目前已踩的步數，n 代表目標步數。
```javascript
var climbStairs= function(i, n) {
    if (i > n) {
        return 0;
    }
    if (i === n) {
        return 1;
    }
    return climbStairs(i + 1, n) + climbStairs(i + 2, n);
}
```
n = 3
```
                              (0,3)
                           /         \
                        (1,3)        (2,3)
                      /       \     /    \
                    (2, 3)  (3,3) (3,3) (4,3)
```
Time complexity: O(2^n)

## Approach #2 Recursion with memorization [Accepted]
Brute force的方法會去遍歷整個recursion tree，我們可以把算出來的數值存到陣列memo裡面，避免重複計算。
```javascript
var memo = [];

var climbStairs= function(i, n) {
    if (i > n) {
        return 0;
    }
    if (i === n) {
        return 1;
    }
    if (memo[i] > 0) {
        return memo[i];
    }
  
    memo[i] = climbStairs(i + 1, n, memo) + climbStairs(i + 2, n, memo);
    return memo[i];
};
```
Time complexity: O(n)

## Approach #3 Dynamic Programming [Accepted]
要到達第i步 = 在i - 1步時再走1步 或 在i - 2步時再走2步
求到達第i步的方法數 = 求出到達 i - 1 的方法數加上到達i - 2的方法數

```javascript
var climbStairs= function(n) {
    if (n === 1) {
        return 1;
    }
    var dp = [];
    dp[1] = 1;
    dp[2] = 2;
    for (var i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    
    return dp[n];
};
```
Time complexity: O(n)
## Approach #4 Fibonacci Number [Accepted]:
Fib(n) = Fib(n−1) + Fib(n−2)
```javascript
var climbStairs = function(n) {
    if (n <= 1)  return 1;
  
    var current = 1;
    var prev = 1;
  
    // fibonacci number: f(n) = f(n - 1) + f(n - 2)
    for (var i = 2; i <= n; i++) {
      var temp = current;
      current = current + prev;
      prev = temp;
    }
  
    return current;
};
```
Time complexity: O(n)