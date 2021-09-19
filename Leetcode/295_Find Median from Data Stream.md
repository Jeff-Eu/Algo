# 295. Find Median from Data Stream
Q: Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
```
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5
```
Design a data structure that supports the following two operations:
* void addNum(int num) - Add a integer number from the data stream to the data structure.
* double findMedian() - Return the median of all elements so far.
 

Example:
```
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
```
Follow up:
* If all integer numbers from the stream are between 0 and 100, how would you optimize it?
* If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

## Answer

* 詳解介紹很多種解法，第一種是最簡單的方法大家都想得到就不介紹了，下面是看過第二種 binary search的解法後改寫 addNum() 裡的 code，注意，用 binary search 做 insert 的問題接近於 Leetcode 35. Search Insert Position,不可輕忽，因為有插入值大於所有陣列元素的情況，以及插入至空集合的情況。 boundary case的問題可以縮小成只有兩個元素時來再來微改code。

* 詳解還有其他厲害的解法，有時間再研究
```python
# Runtime: 276 ms, faster than 53.52% of Python online submissions for Find Median from Data Stream.
# Memory Usage: 25.9 MB, less than 30.89% of Python online submissions for Find Median from Data Stream.
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ls = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        ls = self.ls

        ''' Linear search
        size = len(ls)
        for i in xrange(size):
            if ls[i] > num:
                ls.insert(i, num)
                return
        
        ls.append(num)
        '''
             
        # Binary search
        size = len(ls)
        lo = 0
        hi = size-1
        if not ls or num > ls[hi]:
            ls.append(num)
            return
        
        while lo < hi:
            mid = (lo+hi)/2
            
            if ls[mid] < num:
                lo = mid+1
            elif ls[mid] >= num:
                hi = mid
            else:
                lo = mid
                break
                
        ls.insert(lo, num)
        
    def findMedian(self):
        """
        :rtype: float
        """
        size = len(self.ls)
        half = size / 2
        if size % 2 == 1:
            return self.ls[half]
        else:
            return float(self.ls[half] + self.ls[half-1])/2
```
注意上面 addNum 的時間複雜度分析如下：

Time complexity: O(n) + O(log n) ~≈ O(n).

Binary Search takes O(logn) time to find correct insertion position.
Insertion can take up to O(n) time since elements have to be shifted inside the container to make room for the new element.