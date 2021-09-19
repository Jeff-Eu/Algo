# 322. Coin Change
Q: You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```
Example 2:
```
Input: coins = [2], amount = 3
Output: -1
```
Example 3:

```
Input: coins = [1], amount = 0
Output: 0
```
Example 4:

```
Input: coins = [1], amount = 1
Output: 1
```
Example 5:
```
Input: coins = [1], amount = 2
Output: 2
```

## Answer
* [這位youtuber有很清楚的教學](https://www.youtube.com/watch?v=H9bfqozjoqs)(看完後要想到top-down的方式很簡單，不過他影片倒數第二節想要講bottom-up的方式，講得不夠清楚)，還是要搭配一下詳解最後用 bottom up 的 DP 提出來的遞迴數學公式。

* 注意這題的 bottom up 的 DP 解的迴圈寫法會有點難想像的出來，是一種比較直覺的想法，不需花太久做出詳細證明，以掌握大方向理解並記憶這種寫法為主。
    * 另外這種迴圈的寫法不知道能否應用到排列組合的問題，取代掉遞迴寫法，因為觀察到它的遞迴公式是 min(a1, a2, ..., aN)  也就是同時比較好多個。
        => 應該不行，因為排列組合的比較元素是動態增加的。

影片教學youtuber寫的code如下，效率稍微差一點點，但卻是比詳解code較好理解的bottom-up方式。
```python
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for x in range(1, amount + 1):
            for coin in coins:
                if x-coin >= 0:
                    dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 
```

詳解的code：
```python
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 
```