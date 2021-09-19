# 414. Third Maximum Number

Q: Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
```
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.
```
Example 2:
```
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
```
Example 3:
```
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
```

# Answer
Jeff's

這題是在考Heap觀念的理解深度，如果只會用heap的library，就會被看破手腳

* 要了解 heap 的資料結構，[可以參考這部影片](https://www.youtube.com/watch?v=HqPJF2L5h9U)
    * heap 可以做出 priority queue
    * heap 雖然是樹的資料結構，但一般都是用陣列來表示，才有快速計算的作用
    * heap 的高度就是比較的次數，可用來計算時間複雜度
    * heapify 是將一個non-heap的陣列變成heap，只使用 O(n)的時間；比一個個insert的方法總共要 O(nlogn)的時間還要再快
    
```python
import heapq
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heap = []
        hashset = set()
        
        for n in nums:            
            if n in hashset:
                continue
            else:
                heapq.heappush(heap, n)
                hashset.add(n)
            
            if len(heap) > 3:
                heapq.heappop(heap)
                
        size = len(heap)
        if size == 3 or size == 1:
            return heap[0]
        else:
            return heap[1]
```