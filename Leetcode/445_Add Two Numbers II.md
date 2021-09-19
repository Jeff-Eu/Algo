# 445. Add Two Numbers II
Q: You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Follow up:**
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
```
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
```
## Answer
Jeff's
Use two stacks to reverse the two lists.
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
            
        c = 0
        curr = ListNode(0)
        while True:
            s = 0
            if s1:
                s = s1.pop()
            if s2:
                s += s2.pop()
            if c>0:
                s += c
                
            if s>9:
                curr.val = s - 10
                c = 1
            else:
                curr.val = s
                c = 0
            if s1 or s2 or c>0:
                # Note it's different from the "Add Two Numbers" v.1 problem.
                # The list order should be reversed !
                tmp = curr
                curr = ListNode(0)
                curr.next = tmp
            else:
                break
        return curr
```