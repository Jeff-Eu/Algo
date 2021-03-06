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
以下代碼的註解參考了[高手解](https://leetcode-cn.com/problems/non-overlapping-intervals/solution/wu-zhong-die-qu-jian-ji-bai-liao-100de-y-kkzr/)，比官網解還好。

Sorting Interval[0] in ascending order is O(nlogn), then traversing intervals array is O(n). Total is O(nlogn).

為什麼要先排序？可先參考 57_Insert_interval[反向連結]解說交集聯集的定理

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

複雜度：

c++版本
```cpp
bool comp(vector<int> &a,vector<int> &b) {
	return a[0]<b[0];
}

class Solution {
public:
	int eraseOverlapIntervals(vector<vector<int>>& intervals) {
		int ans=0;      
		if(intervals.size()==0) return 0;
		// You can also ignore the comp in this case.
		sort(intervals.begin(),intervals.end(),comp); 
		int end = intervals[0][1];

		for(int i=1; i<intervals.size(); i++) {
			if(end > intervals[i][0]) {
				ans++;
                end = min(intervals[i][1], end);
			}else 
                end = intervals[i][1];
		}
		return ans;    
	}
};
```

論譠還有一個解法(C++)是用end先排序，感覺也不錯
Actually, the problem is the same as "Given a collection of intervals, find the maximum number of intervals that are non-overlapping." (the classic Greedy problem: [Interval Scheduling](https://en.wikipedia.org/wiki/Interval_scheduling#Interval_Scheduling_Maximization)). 

```cpp
bool comp(vector<int> &a,vector<int> &b) {
	return a[1]<b[1];
}
class Solution {
public:
	int eraseOverlapIntervals(vector<vector<int>>& intervals) {
		int ans=-1;      
		if(intervals.size()==0) return 0;       
		//custom comperator is used.
		sort(intervals.begin(),intervals.end(),comp); 
		vector<int> prev= intervals[0];

		for(vector<int> i: intervals) {
			if(prev[1]>i[0]) {
				ans++; //we dont update previous, because i[1] will be grater then prev[1]
			}else prev=i; // we want the end point to be minimum
		}
		return ans; //ans was initially made -1 because our prev and intervals[0] will always match
	}
};
```


#medium