# 986. Interval List Intersections
Q: You are given two lists of closed intervals, `firstList` and `secondList`, where `firstList[i] = [starti, endi]` and `secondList[j] = [startj, endj]`. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:
```
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```
Example 2:
```
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
```
Example 3:
```
Input: firstList = [], secondList = [[4,8],[10,12]]
Output: []
```
Example 4:
```
Input: firstList = [[1,7]], secondList = [[3,10]]
Output: [[3,7]]
``` 
## Answer
沒看詳解，利用57學到的技巧，跟經過253. Meeting Rooms II 自創解的殘酷洗禮，輔助創造出首刷暴力法是 O(M*N) ，修改後是 O(M+N)，雖然比詳解快，但理解跟實戰性來說詳解的比較好
```python
# Runtime: 116 ms, faster than 93.84% of Python online submissions for Interval List Intersections.
# Memory Usage: 14.6 MB, less than 14.48% of Python online submissions for Interval List Intersections.
class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        # O(M+N) Approach
        ls1, ls2 = firstList, secondList
        cross = []
        size1 = len(ls1)
        idx1 = 0
        for np in ls2: # np is new pair
            us, ue = np[0], np[1]
            
            for i in xrange(idx1, size1):
                p = ls1[i]
                if p[1] < us:
                    continue
                elif p[0] > ue:
                    break
                else:
                    idx1 = i
                    cs = max(us, p[0])
                    ce = min(ue, p[1])
                    cross.append([cs, ce])

        return cross
        
        # O(M*N) Approach
#         ls1, ls2 = firstList, secondList
#         npairs = ls2
#         cross = []
#         for np in npairs:
#             us, ue = np[0], np[1]
            
#             for i in ls1:
#                 if i[1] < us:
#                     continue
#                 elif i[0] > ue:
#                     break
#                 else:
#                     # for cross
#                     cs = max(us, i[0])
#                     ce = min(ue, i[1])
#                     cross.append([cs, ce])

#         return cross
```

詳解的文字說明不太好，但程式碼很好，可以搭配原題的圖片，就容易理解。

詳解的代碼：
```python
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans
```
