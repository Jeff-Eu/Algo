# 414. Third Maximum Number
Q: Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:
```
Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.
```
Example 2:
```
Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
```
Example 3:
```
Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
```
## Answer

Jeff's Python O(N) solution because [heapify's time just costs O(N)](https://stackoverflow.com/questions/51735692/python-heapify-time-complexity).
```python
# Runtime: 32 ms, faster than 93.97% of Python online submissions for Third Maximum Number.
# Memory Usage: 14.3 MB, less than 92.00% of Python online submissions for Third Maximum Number.
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            nums[i] = -nums[i]
            
        heapq.heapify(nums)
        hp = nums
        c = 0
        mx = -hp[0]
        ans = 0.5 # non integer
        while c < 3 and hp:
            tmp = heapq.heappop(hp)
            if ans != tmp:
                ans = tmp
                c += 1
        if c == 3:
            return -ans
        else:
            return mx
```

* 本來想把我寫的python轉成Kotlin，但遇到兩個問題:
    * Leetcode的 compiler不支援 static method，導致我不能用 Comparator.reversed()傳進 PriorityQueue裡，導致我只能用負值存進去。
    * test input 有32bits的最大正數，導致一變負號就overflow，所以結果就錯了。

因此參考了高手java解轉成Kotlin如下
```java kotlin
class Solution {
    fun thirdMax(nums: IntArray): Int {
        var max1: Int? = null
        var max2: Int? = null
        var max3: Int? = null
        for (n in nums) {
            if (n == max1 || n == max2 || n == max3) continue
            if (max1 == null || n > max1) {
                max3 = max2
                max2 = max1
                max1 = n
            } else if (max2 == null || n > max2) {
                max3 = max2
                max2 = n
            } else if (max3 == null || n > max3) {
                max3 = n
            }
        }
        return max3 ?: max1!!
    }
}
```