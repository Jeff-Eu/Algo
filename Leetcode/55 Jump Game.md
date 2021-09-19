# 55. Jump Game

Given an array of non-negative integers `nums`, you are initially positioned at the **first index** of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

**Constraints:**

- `1 <= nums.length <= 3 * 104`
- `0 <= nums[i] <= 105`

## Answer

二刷，一送即過，這是 O(N^2)的解法，詳解還有更快的 O(N) 的Greedy解法。

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        sz = len(nums)
        dp = [False]*sz
        dp[0] = True
        for i in range(1, sz):
            for j in range(i-1, -1, -1):
                if dp[j] and (j + nums[j] >= i):
                    dp[i] = True
                    break
                    
        return dp[sz-1]
    
'''reasoning
dp[j] ==

dp[j-1] and (j-1 + nums[j-1] >= j) or
dp[j-2] and (j-2 + nums[j-2] >= j) or
...
dp[0] and (0 + nums[0] >= j)

Time: O(N^2) where N is the size of nums
'''
```

## Archived

- 詳解除了最後Greedy的方法都算解釋的很好(Greedy的方法大概只要看它的表格就能懂，我在這後面會用更好的解釋),下面詳解的四種解法都有連續性，逐步變成更好的解法。
- 遞迴的function可能就有機會用 DP 記錄起來。

Approach 1: Backtracking

```java
public class Solution {

    public boolean canJumpFromPosition(int position, int[] nums) {
        if (position == nums.length - 1)
            return true;

        int furthestJump = Math.min(position + nums[position], nums.length - 1);
        for (int nextPosition = position + 1; nextPosition <= furthestJump; nextPosition++)
            if (canJumpFromPosition(nextPosition, nums))
                return true;

        return false;
    }

    public boolean canJump(int[] nums) {
        return canJumpFromPosition(0, nums);
    }
}
```

Approach 2: Dynamic Programming Top-down

```java
enum Index {
    GOOD, BAD, UNKNOWN
}

public class Solution {
    Index[] memo;

    public boolean canJumpFromPosition(int position, int[] nums) {
        if (memo[position] != Index.UNKNOWN)
            return memo[position] == Index.GOOD ? true : false;

        int furthestJump = Math.min(position + nums[position], nums.length - 1);
        for (int nextPosition = position + 1; nextPosition <= furthestJump; nextPosition++) {
            if (canJumpFromPosition(nextPosition, nums)) {
                memo[position] = Index.GOOD;
                return true;
            }
        }

        memo[position] = Index.BAD;
        return false;
    }

    public boolean canJump(int[] nums) {
        memo = new Index[nums.length];
        for (int i = 0; i < memo.length; i++)
            memo[i] = Index.UNKNOWN;

        memo[memo.length - 1] = Index.GOOD;
        return canJumpFromPosition(0, nums);
    }
}
```

Approach 3: Dynamic Programming Bottom-up

```java
// 1. The recursion is usually eliminated by trying to reverse the order of the steps from the top-down approach.
// 2. 注意這方法都不會設 memo[i] 為 BAD// 3. The observation to make here is that we only ever jump to the right. This means that if we start from the right of the array, every time we will query a position to our right, that position has already be determined as being GOOD or BAD. This means we don't need to recurse anymore, as we will always hit the memo table.
enum Index {
    GOOD, BAD, UNKNOWN
}

public class Solution {
    public boolean canJump(int[] nums) {
        Index[] memo = new Index[nums.length];
        for (int i = 0; i < memo.length; i++)
            memo[i] = Index.UNKNOWN;

        memo[memo.length - 1] = Index.GOOD;

        for (int i = nums.length - 2; i >= 0; i--) {
            int furthestJump = Math.min(i + nums[i], nums.length - 1);
            for (int j = i + 1; j <= furthestJump; j++) {
                if (memo[j] == Index.GOOD) {
                    memo[i] = Index.GOOD;
                    break;
                }
            }
        }

        return memo[0] == Index.GOOD;
    }
}
```

Approach 4: Greedy (最快，O(N)解法)

```java
// Runtime: 60 ms, faster than 93.60% of Python online submissions for Jump Game.
// Memory Usage: 15.7 MB, less than 8.10% of Python online submissions for Jump Game.
public class Solution {
    public boolean canJump(int[] nums) {
        int lastPos = nums.length - 1;
        for (int i = nums.length - 1; i >= 0; i--)
            if (i + nums[i] >= lastPos)
                lastPos = i;

        return lastPos == 0;
    }
}
```

Greedy解的口述解釋技巧：利用 *range cover的概念* 來說明

```
idx  0 1 2 3 4
val  2 3 0 1 4 
mark   T F T T  
```