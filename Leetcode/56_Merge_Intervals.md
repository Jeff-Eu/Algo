# 56. Merge Intervals
Q: Given a collection of intervals, merge all overlapping intervals.

Example 1:
```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```
Example 2:

```
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

## Answer

* 先對interval array依照start由小到大做排序
* 取interval array第一筆的start、end屬性
* 跑迴圈去比較是否有重疊

c++參考首刷
```cpp
// Runtime: 8 ms, faster than 99.93% of C++ online submissions for Merge Intervals.
bool comp(vector<int>& a, vector<int>& b) {
    return a[0] < b[0];
}
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), comp);
        
        vector<vector<int>> merged;
        for(auto& v : intervals) {
            if(merged.empty() == false && merged.back()[1] >= v[0]) {
                merged.back()[1] = max(v[1], merged.back()[1]);
            }else
                merged.push_back(v);
        }
        
        return merged;
    }
};
```
Ref: 
* [C++ auto& vs auto](https://stackoverflow.com/questions/29859796/c-auto-vs-auto)
* [C++ 程式語言 auto 自動變數類型語法教學與範例](https://blog.gtwang.org/programming/cpp-auto-variable-tutorial/)

Complexity: O(N*Log(N))

Jeff's 二刷 (better and easier)
```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
            
        intervals.sort(key=lambda x: x[0])
        
        out = []
        for part in intervals:
            if out and out[-1][1] >= part[0]:
                out[-1][1] = max(out[-1][1], part[1])
            else:
                out.append(part)
        
        return out
```

Jeff's 一刷
```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        # 注意 comparer的寫法
        ln = sorted(intervals, cmp=self.compare)
        
        i = 0
        out = [ln[0]]
        for part in ln:
            if out[i][1] >= part[0]:
                # can merge
                if out[i][1] < part[1]:
                    out[i][1] = part[1]
            else:
                out.append(part)
                i += 1
        return out
            
        
    def compare(self, l1, l2):
        if l1[0] < l2[0]:
            return -1
        elif l1[0] > l2[0]:
            return 1
        else:
            return 0
```

舊版函式定義的題目的解:

Jeff's 舊版解(not good because not sorting first):
```python
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        result = []
        for i in intervals:
            result = self.insert(result, i)
        return result


    def insert(self, inList, newItem):
        outList = []
        isNewAdded = False
        for interval in inList:
            s = self.intersect(newItem.start, interval)
            e = self.intersect(newItem.end, interval)
            
            if s < 0:
                outList.append(interval)
            elif s == 0:
                outList.append(newItem)
                newItem.start = interval.start
                isNewAdded = True
            else:
                if isNewAdded == False:
                    outList.append(newItem)
                    isNewAdded = True

            if e == 0:
                newItem.end = interval.end
            elif e > 0:
                outList.append(interval)

        if isNewAdded == False:
            outList.append(newItem)

        return outList

    '''
        return 
        -1: interval is before pos
         0: interval covers the pos
         1: interval is after pos
    '''
    def intersect(self, pos, interval):
        if interval.end < pos:
            return -1
        elif interval.start > pos:
            return 1
        else:
            return 0
```


學平's Approach #1 [Accepted]
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
 * @return {Interval[]}
 */
var merge = function(intervals) {
    intervals.sort(function(a, b) {
        if (a.start < b.start) {
            return -1;
        } else if (a.start > b.start) {
            return 1;
        } else {
            return 0;
        }
    });
    
    var result = [];
    if (intervals.length === 0) return result;
    var start = intervals[0].start;
    var end = intervals[0].end;
    
    
    for (var i = 0; i < intervals.length; i++) {
        if (intervals[i].start <= end) { // overlapping
            end = Math.max(end, intervals[i].end);
        } else { // disjoint
            result.push(new Interval(start, end));
            start = intervals[i].start;
            end = intervals[i].end;
        }
    }
    // Add the last interval
    result.push(new Interval(start, end));
    return result;
};
```

# Relation
進階->[[57_Insert_interval]]


#medium