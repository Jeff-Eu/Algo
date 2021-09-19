# 19. Remove Nth Node From End of List
Q: Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```
Example 2:
```
Input: head = [1], n = 1
Output: []
```
Example 3:
```
Input: head = [1,2], n = 1
Output: [1]
``` 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

## Answer
[用InterviewBit的平台](https://www.interviewbit.com/problems/remove-nth-node-from-list-end/#)再刷一次
```python
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        
        if not A:
            return A
        ls = []
        head = A
        pre = ListNode(0)
        pre.next = head
        ls.append(pre)
        while head:
            ls.append(head)
            head = head.next
            
        n = len(ls) - B
        
        if n >= 1:
            ls[n-1].next = ls[n].next
        else:
            ls[0].next = ls[1].next

        return pre.next
```

下面是我想到的One-Pass解法，可以跟下一個解法比較，下一個解法是一般會想到的基本解法，比較兩者的code，可發現第一種解的複雜度為 O(2N), 第二種為 O(N+3M)，其中M是要移除的元素從頭數來第幾個位置，
如果 N>3M 則第一種的解法較慢。

```python
# Runtime: 16 ms, faster than 91.47% of Python online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.4 MB, less than 42.79% of Python online submissions for Remove Nth Node From End of List.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lis=[]

        preHead = ListNode(0)
        preHead.next = head
        lis.append(preHead)
        
        while head:
            lis.append(head)
            head=head.next

        idx = len(lis)-n
        
        lis[idx-1].next = lis[idx].next
        return preHead.next
```        

java版
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ArrayList<ListNode> ls = new ArrayList();
        
        ListNode preHead = new ListNode(0);
        preHead.next = head;
        ls.add(preHead);
        
        while(head != null) {
            ls.add(head);
            head = head.next;
        }
        
        int idx = ls.size() - n;
        ls.get(idx-1).next= ls.get(idx).next;
        return preHead.next;
    }
}
```

一般會想到的基本解法
```python
# Runtime: 20 ms, faster than 70.21% of Python online submissions for Remove Nth Node From End of List.
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lis=[]

        head2 = head

        size=0
        while head:
            size+=1
            head=head.next

        idx = size-n
        
        pre = ListNode(0)
        pre.next = head2
        pre2=pre
        while idx>0:
            idx-=1
            pre=pre.next
            head2=head2.next
        
        pre.next=head2.next
        return pre2.next        
```