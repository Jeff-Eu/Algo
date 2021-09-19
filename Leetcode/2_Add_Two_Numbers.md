# 02. Add Two Numbers:
Q: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

# Explain
這題是考大數相加，只要快速看懂下圖就能寫得出來
![2 add two nums](imgs\2_add_two_nums.jpg)

# Solution
Jeff's second practice
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
        curr = ListNode(0)
        out = curr
        add = 0
        while True:
            c = 0
            if l1:
                c = l1.val
                l1 = l1.next
            if l2:
                c += l2.val
                l2 = l2.next
            if add > 0:
                c += add

            if c > 9:
                curr.val = c - 10
                add = 1
            else:
                curr.val = c
                add = 0
                
            if l1 or l2 or add > 0:
                curr.next = ListNode(0)
                curr = curr.next
            else:
                break
        
        return out
```

Jeff's answer
```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        lnow = ListNode(-1)
        lresult = lnow

        while (l1 is not None) or (l2 is not None) or carry != 0:
            
            v1, v2 = 0, 0
            if l1 is not None:
                v1 = l1.val
            if l2 is not None:
                v2 = l2.val

            v = v1 + v2 + carry
            carry = 0

            if v >= 10:
                carry = 1
                v -= 10

            lnow.next = ListNode(v)
            lnow = lnow.next

            if l1 != None:
                l1 = l1.next
            
            if l2 != None:
                l2 = l2.next

        lresult = lresult.next

        return lresult

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
s = Solution()
r = s.addTwoNumbers(l1, l2)
print r.val, r.next.val, r.next.next.val
```