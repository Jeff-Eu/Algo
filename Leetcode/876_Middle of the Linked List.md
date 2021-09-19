# 876. Middle of the Linked List
Q: Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Example 1:
```
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
```
Example 2:
```
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
```
## Answer
解一：
```python
#     Runtime: 16 ms, faster than 70.43% of Python online submissions for Middle of the Linked List.
# Memory Usage: 13.5 MB, less than 62.70% of Python online submissions for Middle of the Linked List.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = 0
        h2 = head
        while head:
            n += 1
            head = head.next

        n = n/2
        for _ in xrange(n):
            h2 = h2.next

        return h2
```
最佳解在下面解二的快慢指針法，比較上下兩個解法的Time Complexity，如果只針對while去計算，會發現上面做了 3*n + 2*n/2 = 4n (我想xrange裡可能每次是跑2，但我先暫用1)；而下面做了 (2+1+2)*n/2 = 2.5n


**番外補充(不重要)**: 可以看得出來，現在是取一半，所以會除以2，如果是超過2的數字，且愈大的話(令m，而 m最大為 n)，第二種算法的Time愈變成
```
(1+(m-1)+1+1)*n/m = (m+2)*n/m ~= n
           ^ 因為前面的 m-1 次可以取最後一個fst.next...next 存成一個變數去重覆使用，就不用再呼叫那麼長也耗時
```
而第一種算法會是 3*n + 2*n/m ~= 3n ，兩者速度差距也變更大了些。 

解二(快慢指針法(最佳))：
```python
# Runtime: 8 ms, faster than 99.26% of Python online submissions for Middle of the Linked List.
# Memory Usage: 13.6 MB, less than 8.96% of Python online submissions for Middle of the Linked List.
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slw = fst = head
        
        while fst and fst.next:
            slw = slw.next
            fst = fst.next.next
            
        return slw
```   