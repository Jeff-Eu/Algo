## 256_Paint House (locked)
Q: Description
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color, and you need to cost the least. Return the minimum cost.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, `costs[0][0]` is the cost of painting house 0 with color red; `costs[1][2]` is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

## Answer

題目在: https://www.lintcode.com/problem/515

隔天以後的首刷，約花16分鐘才想出來，共約29分才寫出來。

從這題可以知道，dp不一定就是最後output出來的答案，像這題是三個dp解的最小值才是答案。

原來這種 DP是屬於 Coordinate DP。
```python 3
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        
        if not costs:
            return 0
            
        n = len(costs)
        dp = [[float("inf") for _ in range(3)] for _ in range(n)]
        
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        for i in range(1, n):
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
            
        return min(dp[n-1][0], dp[n-1][1], dp[n-1][2])
```

高手解
```java
public class Solution {
    /**
     * @param costs: n x 3 cost matrix
     * @return: An integer, the minimum cost to paint all houses
     */
    public int minCost(int[][] costs) {
    if(costs==null||costs.length==0)
        return 0;
 
    for(int i=1; i<costs.length; i++){
        costs[i][0] += Math.min(costs[i-1][1], costs[i-1][2]);
        costs[i][1] += Math.min(costs[i-1][0], costs[i-1][2]);
        costs[i][2] += Math.min(costs[i-1][0], costs[i-1][1]);
    }
 
    int m = costs.length-1;
    return Math.min(Math.min(costs[m][0], costs[m][1]), costs[m][2]);
}
}
```

## Archived

首刷,20分，超時窮舉法
```python
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
    # [[14,2,11],[11,14,5],[14,3,10]]
    # [[1,2,3],[1,4,6]]
    
        if not costs:
            return 0
            
        ans = [float("inf")]
        
        n = len(costs)
        def dfs(d, idx, cost):
            
            cost += costs[d][idx]
            if d==n-1:
                if ans[0] > cost:
                    ans[0] = cost
                return
            
            for i in xrange(3):
                if i != idx:
                    dfs(d+1, i, cost)
            
            
        for i in xrange(3):
            dfs(0, i, 0) # depth, branch

        return ans[0]
```