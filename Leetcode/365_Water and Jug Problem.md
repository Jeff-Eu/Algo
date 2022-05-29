# 365. Water and Jug Problem
You are given two jugs with capacities `jug1Capacity` and `jug2Capacity` liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly `targetCapacity` liters using these two jugs.

If `targetCapacity` liters of water are measurable, you must have `targetCapacity` liters of water contained **within one or both buckets** by the end.

Operations allowed:

-   Fill any of the jugs with water.
-   Empty any of the jugs.
-   Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.

**Example 1:**

**Input:** jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
**Output:** true
**Explanation:** The famous [Die Hard](https://www.youtube.com/watch?v=BVtQNK_ZUJg&ab_channel=notnek01) example 

**Example 2:**

**Input:** jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
**Output:** false

**Example 3:**

**Input:** jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
**Output:** true

**Constraints:**

-   `1 <= jug1Capacity, jug2Capacity, targetCapacity <= 106`

## Answer
* 這題使用到 Bézout's identity貝祖定理 https://leetcode.com/problems/water-and-jug-problem/discuss/83715/Math-solution-Java-solution
	* 推文也有提到一個滿有趣的現象，雖然跟GCD的解法無關
	 https://www.youtube.com/watch?v=0Oef3MHYEC0 

不過話說回來，雖然用貝祖定理可以解釋 ax+by=m 是否有整數解，但還沒看到有人解釋為何這題倒水的順序用 ax+by=m 的整數解在實際上是可行的。這背後又是一個值得研究的問題 - todo。

而且，這題目還有個問題，因為題目說 "If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end."，那貝氏定理的例子是

3x + 4y = 26

兩個桶子加起來也不會大於26
故題目應再稍作修改

另外論譠上也有人用 tree的方式解，應該算是不用到數論，實際操作的寫法，尚未研究 - todo。
 
```python
class Solution(object):
    def canMeasureWater(self, jug1, jug2, target):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """
        if jug1 + jug2 < target:
            return False
        
        
        def gcd(a, b):
            
            r = a%b
            while r!=0:
                a=b
                b=r
                r=a%b
            return b
        
        return target % gcd(jug1, jug2) == 0
```