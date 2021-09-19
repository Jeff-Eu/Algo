# 435. Non-overlapping Intervals
Q: Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
```
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
```
Example 2:
```
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
```
Example 3:
```
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
``` 

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

## Answer
以下代碼的註解參考了[高手解](https://leetcode-cn.com/problems/non-overlapping-intervals/solution/wu-zhong-die-qu-jian-ji-bai-liao-100de-y-kkzr/)，比官網解還好

```python
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        
        size = len(intervals)
        c = 0
        end = intervals[0][1]
        for i in xrange(1, size):
            if end > intervals[i][0]: # overlap
                # 如果重叠了，必须要移除一个，所以count要加1，
                # 然后更新尾部的位置，我们取尾部比较小的
                end = min(end, intervals[i][1])
                c+=1
            else:
                # 如果没有重叠，就不需要移除，只需要更新尾部的位置即可
                end = intervals[i][1]
                
        return c
```