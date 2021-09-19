# 252. Meeting Rooms (付費解鎖題)

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example
Example1
```
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict
```
Example2
```
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 
```


## Answer

* 主要必須判斷各interval之間是否有重疊, 若有重疊則 return false
* 先把intervals對其start值由小到大做排序, 以方便之後判斷重疊

Jeff's
```python
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        
        intervals.sort(key=lambda x: x.start)
        
        size = len(intervals)
        for i in xrange(0, size-1):
            if intervals[i].end > intervals[i+1].start:
                return False
                
        return True
```

```javascript
/**
 * Definition for an interval.
 * function Interval(start, end) {
 *     this.start = start;
 *     this.end = end;
 * }
 */
/**
 * @param {Interval[]} intervals
 * @return {boolean}
 */
var canAttendMeetings = function(intervals) {
    
    intervals.sort(function(a, b) {
        return a.start - b.start;
    });
    
    for (var i = 1; i < intervals.length; i++) {
        if (intervals[i].start < intervals[i - 1].end) { // overlapping
            return false;
        }
    }
    
    return true;
};
```