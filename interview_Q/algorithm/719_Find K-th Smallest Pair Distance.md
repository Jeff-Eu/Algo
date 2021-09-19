# 719. Find K-th Smallest Pair Distance
Q: Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
```
Input:
nums = [1,3,1]
k = 1
Output: 0 
```
Explanation:
```
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
```
Note:
1. 2 <= len(nums) <= 10000.
2. 0 <= nums[i] < 1000000.
3. 1 <= k <= len(nums) * (len(nums) - 1) / 2.

## Answer
這題算是binary search裡的難題，雖然LC有詳解但也很難理解，下面記錄最佳解的code，也是最易理解的版本。

```python
class Solution(object):
    def smallestDistancePair(self, nums, k):
        # Let possible(guess) be true if and only if there are k or more pairs with distance less than or equal to guess.
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            # Notice the skill of "Moving Window" used here
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        N = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid, N):
                hi = mid
            else:
                lo = mid + 1

        return lo
```