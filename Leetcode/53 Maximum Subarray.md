# 53. Maximum Subarray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return *its sum*.

**Example 1:**

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Example 2:**

```
Input: nums = [1]
Output: 1
```

**Example 3:**

```
Input: nums = [5,4,-1,7,8]
Output: 23
```

**Constraints:**

- `1 <= nums.length <= 3 * 104`
- `105 <= nums[i] <= 105`

**Follow up:**

If you have figured out the

```
O(n)
```

solution, try coding another solution using the

**divide and conquer**

approach, which is more subtle.

## 思路

這題的觀念屬於困難等級，利用到Dynamic Programming的技巧，屬於大師解題，說明如[Wikipedia](https://en.wikipedia.org/wiki/Maximum_subarray_problem)(2020/1/27 update: wiki更新後無論中英文在講解這演算法都很不清楚，直接看虛擬碼會省很多時間)。但這題在面試時也常被拿來考，且Leetcode上答對人數有39.4%，不得不做先理解及記憶。

說明：這裡表示的A[j]是代表在A陣列的第j個元素。

解這題的演算法會需要儲存兩種max值，一個是局部max(命名為m)，一個是絕對max(命名為M)，以數列A[1...n]來說明，演算法會從最左邊開始掃描，A[1...j], j=1，接下來才是j=2，<u>局部max指是結尾在j的最大子陣列</u>，每次找到m再去更新M。為何要找局部max？以掃描到第j個為例，它是結尾在j的最大子陣列，那下次掃描進到j+1時，我們要看看包含了j+1的新可能子陣列(<u>同時也是結尾在j+1</u>)，是不是能找到新的絕對max，但是要包含j+1的子陣列除了它自己，也需考慮跟它相連也必包含第j的子陣列，結尾在j+1的子陣列最大的只有可能是 A[j+1] 與 m + A[j+1]，你可能會懷疑為什麼會有 m + A[j+1]？ 因為m已經是 A[1...j]結尾在第j中，最大的子陣列了，會跟A[j+1]相連的子陣列若不為空，最大的只有它。

## **面試資訊**

- 面試出題:
    - 美商 Arlo Technologies
    - Facebook, Yahoo, PayPal, M$, LinkedIn

## Solution
Kotlin
```java kotlin
class Solution {
    fun maxSubArray(nums: IntArray): Int {
        
        val sz = nums.size
        var mxi = nums[0] // max value of a subarray which ends at index i of nums
        var ans = nums[0]
        for(i in 1..sz-1) {
            
            mxi = maxOf(mxi+nums[i], nums[i])
            ans = maxOf(ans, mxi) 
        }
        
        return ans
    }
}
```

Java

```java
// Runtime: 0 ms, faster than 100.00% of Java online submissions for Maximum Subarray.
class Solution {
    public int maxSubArray(int[] nums) {

        int end = nums[0];
        int max = end;

        for(int i=1; i<nums.length; i++) {

            end = Math.max(nums[i], end + nums[i]);
            max = Math.max(max, end);
        }

        return max;
    }
}
```

Python

```python
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, nums):
        max_ending_here = max_so_far = nums[0]
        # Python: What does for x in A[1:] mean?
        #   https://stackoverflow.com/a/44341431/1613961
        for x in nums[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

# 短寫法
class Solution(object):
    def maxSubArray(self, nums):

        M = m = nums[0]

        for a in nums[1:]:
            m = max(a, m + a)
            M = max(M, m)
        return M
```

複刷Java(較慢)

```java
// Runtime: 0 ms, faster than 44% of Java online submissions for Maximum Subarray.
class Solution {
    public int maxSubArray(int[] nums) {
        int amax = nums[0];
        int dp[] = new int[nums.length];

        dp[0] = nums[0];
        for(int i=1; i<nums.length; i++) {
            int lmax = Math.max(nums[i], dp[i-1]+nums[i]);
            if(lmax > amax)
                amax = lmax;
            dp[i] = lmax;
        }
        return amax;
    }
}

/*
dp[k] = max subarray ending at k
    = max(dp[k-1], k)
*/
```