# 253. Meeting Rooms II (locked)
Q: Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example1:
```
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
```
Example2:
```
Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
```
## Answer
付費題。

在[LintCode Meeting Rooms II
](https://www.lintcode.com/problem/meeting-rooms-ii/my-submissions) 首刷通過, 作圖簡化時發現區間會形成類似"河內塔"的形狀，所以就用這方式去實作。作法是每次有新的區間加入就從第一層開始掃，聯集更新第一層；再將交集的丟給第二層做同樣的動作，再來第三層...以此類推，如果發現到了最高層之後還有交集，代表河內塔可以再多一層，就降把每一層的區間都記錄下來，去算總共幾層就是答案，但其實這寫法太複雜，而且交集的部分應該可以再最佳化，總之不太適合實戰，所以暫時不想講太仔細了。不過這作法可以將不同重疊次數的區間全都記錄下來，還沒找到題目可以驗證我的code，但在這題至少是通過了。

河內塔示意圖\
![](imgs\253_1.png)

河內塔法(自創名)：
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
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals:
            return 0
        pairs = intervals
        arr = []
        arr.append([pairs[0]])

        for i, p in enumerate(pairs[1:]):
            size = len(arr)
            ls = [p]
            for i in xrange(size):
                union, cross = self.union_cross(arr[i], ls)
                arr[i] = union
                ls = cross
                if i==size-1 and ls:
                    arr.append(ls)
        # Print Hanoi from bottom to up
        # for ar in arr:
        #     for a in ar:
        #         print (a.start, a.end),
        #     print ""
        
        return len(arr)

    def union_cross(self, intervals, newIntervals):
        npairs = newIntervals
        cross = []
        union = intervals
        for np in npairs:
            us, ue = np.start, np.end
            left, right = [], []
            for i in union:
                if i.end < us:
                    left += i,
                elif i.start > ue:
                    right += i,
                else:
                    # for cross
                    cs = max(us, i.start)
                    ce = min(ue, i.end)
                    cross.append(Interval(cs, ce))
                    # for union
                    us = min(us, i.start)
                    ue = max(ue, i.end)
            union = left + [Interval(us, ue)] + right

        return (union, cross)
```

這題真正好的作法如下，雖然不會將"河內塔區間"記錄下來，但針對問題的解法算很快。

[這youtuber有不錯的解釋](https://www.youtube.com/watch?v=4MEkBvqE_2Q)

我的補充：先針對每個時段的start做排序，這些時段分別用A1, A2, A3,...表示，降就可以想像成，一開始加入第一個時段A1進會議室，那下一個時段A2要加入一定就是找目前會議室時間已經結束的，也就是 A2.start >= A1.end (假設時間點相等時，會議是可以銜接的，比較符合現實生活)，否則就要另外開新的會議室；再來A3也是找前面時段 A1, A2的 end有沒有已經結束的，也就是 A3.start >= A1.end 或 A2.end，如果大於其中一個Ai，那 A3就可加入Ai的會議室，如果兩個都可以加入，我認為，加入任一個最後結果都一樣；但為了計算上的速度，才會每個Ai.end放入 min heap，這樣直接跟最小的end去比，不行的話就不用再比其他的了，如此最省事。

代碼來自[這裡](https://zhenyu0519.github.io/2020/07/13/lc253/#253-meeting-rooms-ii-python)

Time: O(nlogn)

Heap + Sort法：
```python 3
def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        size = len(intervals)
        if size<=1: return size
        heap = []
        for interval in sorted(intervals):
            if heap and interval[0]>=heap[0]:
                heapq.heappushpop(heap,interval[1])
            else:
                heapq.heappush(heap,interval[1])
        return len(heap)
```

