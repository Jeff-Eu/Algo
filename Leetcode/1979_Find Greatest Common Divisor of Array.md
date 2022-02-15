# 1979. Find Greatest Common Divisor of Array
Given an integer array `nums`, return _the **greatest common divisor** of the smallest number and largest number in_ `nums`.

The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.

**Example 1:**

**Input:** nums = [2,5,6,9,10]
**Output:** 2
**Explanation:**
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.

**Example 2:**

**Input:** nums = [7,5,6,8,3]
**Output:** 1
**Explanation:**
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.

**Example 3:**

**Input:** nums = [3,3]
**Output:** 3
**Explanation:**
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.

**Constraints:**

-   `2 <= nums.length <= 1000`
-   `1 <= nums[i] <= 1000`

## Answer
關於GCD，不需要用國中學的展轉相除法那樣去畫圖，其實程式看起來比展轉相除法還簡單。

```python
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mi = nums[0]
        mx = nums[0]
        sz = len(nums)
        for idx in xrange(1, sz):
            if nums[idx] > mx:
                mx = nums[idx]
            elif nums[idx] < mi:
                mi = nums[idx]
                
        def gcd(a, b):
            
            r = a%b
            while r != 0:
                a = b
                b = r
                r = a%b
            return b
                
        return gcd(mx, mi)
```

```java kotlin
class Solution {
    fun findGCD(nums: IntArray): Int {
        
        var mi = nums[0]
        var mx = nums[0]
        val sz = nums.size
        for(idx in 1..sz-1) {
            
            if(nums[idx] < mi)
                mi = nums[idx]
            else if(nums[idx] > mx)
                mx = nums[idx]
        }
        
        fun gcd(a: Int, b: Int): Int {
            
            var r = a%b
            var a2 = a
            var b2 = b
            while(r != 0){
                
                a2 = b2
                b2 = r
                r = a2%b2
            }
            return b2
        }
        
        return gcd(mi, mx)
    }
}
```