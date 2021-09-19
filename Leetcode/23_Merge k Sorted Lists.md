# 23. Merge k Sorted Lists
Q: Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```

## Answer:
這題出得很漂亮，它同時考到 Linked List, Heap, 還有 merge sorted lists 的性質。如果一不小心，可能會忽略了比較最小的值要用 Heap 去解，不只寫法更精簡，而且速度也更快。另外這題感覺也很有應用價值！
Jeff二刷
```python
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """        
        heap = []
        for item in lists:
            if item:
                heapq.heappush(heap, (item.val, item))

        s = r = ListNode(0)
        while heap:
            pair = heapq.heappop(heap)
            r.next = pair[1]
            r = r.next
            nextNode = pair[1].next
            if nextNode:
                heapq.heappush(heap, (nextNode.val, nextNode))

        return s.next
```

Jeff's
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """        
        s = p = ListNode(0)
        
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))

        while heap:    
            mNode = tmp = heapq.heappop(heap)[1]
            mNode = mNode.next
            if mNode:
                heapq.heappush(heap, (mNode.val, mNode))
                
            p.next = tmp
            p = p.next
            
        return s.next
```