# 57. Insert Interval
Q: Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```
Example 2:
```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

# Answer
注意這裡必學三個重要定理，就是如何判斷兩時段是否有交集，以及如何取得交集及聯集，這會在進階版區間問題 253. Meeting Rooms II 應該會很有幫助。

[以下改自力扣官方解](https://leetcode-cn.com/problems/insert-interval/solution/cha-ru-qu-jian-by-leetcode-solution/):

> 對於區間 S1 = [l1, r1] 和 S2 = [l2, r2]，如果它們之間沒有重疊（沒有交集），說明要麼 S1 在 S2 的左側，此時有 r1 < l2 ；要麼 S1 在 S2 的右側，此時有 l1 > r2 。
> 
> 如果S1 不在 S2的左側或右側，即
>
> 定理1:\
> S1 和 S2 必定有交集 <-> `not (r1 < l2 or l1 > r2) = (r1 >= l2 and l1 <= r2 )`
> 
> 定理2:\
> 它們的交集即為
> 
> `[max(l1, l2), min(r1, r2)]`
> 
> 定理3:\
> 並集即為
> 
> `[min(l1, l2), max(r1, r2)]`
> 
> 記法: 交集跟並集都是 "左左，右右"；只是 min 跟 max顛倒；聯集左邊要取最長，所以min用在left，剩下就可以直接推理出來。
> 

從定理1我才了解，為什麼區間問題都要先對start做排序，因為這樣我們的區間要判斷是否"無交集"，就只要比較"區間2是不是在區間1的右側"，也就是只要比較 `r1 < l2`就好。

應用 => Stephan的寫法，非常漂亮！
```python
def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left, right = [], []
    for i in intervals:
        if i.end < s:
            left += i,
        elif i.start > e:
            right += i,
        else:
            s = min(s, i.start)
            e = max(e, i.end)
    return left + [Interval(s, e)] + right
```
不重要的研究：如果上面程式的 intervals是沒有 sort過的，那最後回傳的結果從區間的角度來看算是正確的，但只是沒有按照 start做排序。我的Test程式：
```python
class Solution(object):
    def insert(self, intervals, newInterval):
        pairs = intervals
        pairs.sort(key=lambda p: -p[1]) # 驗證亂排序看結果是否正確
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        for p in pairs:
            if p[1] < s:
                left += [p]
            elif p[0] > e:
                right += [p]
            else:
                s = min(s, p[0])
                e = max(e, p[1])
        ls = left + [[s, e]] + right
        ls.sort() # 最後還是要針對 start作排序
        return ls
```

力扣官方解:
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
                # 与插入区间有交集，计算它们的并集
                left = min(left, li)
                right = max(right, ri)
        
        if not placed:
            ans.append([left, right])
        return ans
```

\
另外參考論譠的改良了"合併區間解"的寫法，使用bisect.insort就可以不用再排序，將速度降到 O(N)
```python
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        def merge(lista):            
            out = []
            for part in lista:
                if out and part[0] <= out[-1][1]:
                    out[-1][1] = max(out[-1][1], part[1])
                else:
                    out.append(part)

            return out
        
        bisect.insort(intervals, newInterval)
        return merge(intervals)
```

Jeff's 二刷 (better to remember)
這題在Leetcode屬於hard，但它的姊妹題 No.56 只有 medium，如果會解 No.56，就可以用 No.56的答案來reuse解出這題，就變得很簡單了

Time: O(NlogN)
```python
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        def merge(lista):
            lista.sort(key=lambda x:x[0]) # 或寫成 lista.sort()
            
            out = []
            for part in lista:
                if out and part[0] <= out[-1][1]:
                    out[-1][1] = max(out[-1][1], part[1])
                else:
                    out.append(part)

            return out
        
        intervals.append(newInterval)
        return merge(intervals)
```

Jeff's 一刷
```python
# 解說圖: http://res.cloudinary.com/yoyoyo3/image/upload/v1496483519/P_20170603_172422_unjmhl.jpg

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        for i in intervals:
            if i.end < newInterval.start:
                result.append(i)
            elif i.start > newInterval.end:
                result.append(newInterval)
                newInterval = i
            else:
                s = min(i.start, newInterval.start)
                e = max(i.end, newInterval.end)
                newInterval = Interval(s, e)
        result.append(newInterval)
        return result
```