# 143. Reorder List
Q: Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
```
Given 1->2->3->4, reorder it to 1->4->2->3.
```
Example 2:
```
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
```
## Answer
這題若要用最佳解，難度算是hard，會同時用到 快慢指針 及 reverse linked list的基本型。

參考了[這裡的圖解](https://leetcode-cn.com/problems/reorder-list/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-34/)
```
主要是三步，举个例子。

1 -> 2 -> 3 -> 4 -> 5 -> 6
第一步，将链表平均分成两半
1 -> 2 -> 3
4 -> 5 -> 6
    
第二步，将第二个链表逆序
1 -> 2 -> 3
6 -> 5 -> 4
    
第三步，依次连接两个链表
1 -> 6 -> 2 -> 5 -> 3 -> 4
```

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)
            
    def middleNode(self, head: ListNode):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head: ListNode):
        if not head:
            return head
        
        curr = head
        while curr.next:
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = head
            head = tmp
        return head

    def mergeList(self, l1, l2):
        while l2:
            tmp = l1.next
            l1.next = l2
            tmp2 = l2.next
            l2.next = tmp
            l1 = tmp
            l2 = tmp2
```
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
    public void reorderList(ListNode head) {
        if (head==null)
            return;
        
        ListNode mid = middleNode(head);
        ListNode l1 = head;
        ListNode l2 = mid.next;
        mid.next = null;
        l2 = reverseList(l2);
        mergeList(l1, l2);
    }
    
    ListNode middleNode(ListNode head) {
        ListNode slw, fst;
        slw = fst = head;
        while(fst != null && fst.next != null){
            slw = slw.next;
            fst = fst.next.next;
        }
        return slw;
    }
    
    ListNode reverseList(ListNode head) {
        if(head==null)
            return head;
        ListNode curr = head;
        while(curr.next!=null){
            ListNode tmp = curr.next;
            curr.next = tmp.next;
            tmp.next = head;
            head = tmp;
        }
        return head;
    }
    
    void mergeList(ListNode l1, ListNode l2){
        while(l2 != null){
            ListNode tmp = l1.next;
            l1.next = l2;
            ListNode tmp2 = l2.next;
            l2.next = tmp;
            l1 = tmp;
            l2 = tmp2;
        }
    }
}
```

看完詳解後首刷
```python
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return head
        
        def reverse(hd):
            if not hd:
                return hd
            curr = hd
            while curr.next:
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = hd
                hd = tmp
            return hd
            
        # Find middle & split into two lists
        fst = slw = head
        while fst and fst.next:
            fst = fst.next.next
            slw = slw.next
        mid = slw
        head2 = mid.next
        mid.next = None

        # Reverse the second list
        head2 = reverse(head2)
        
        # merge two lists!
        while head2:
            t1 = head.next
            head.next = head2
            t2 = head2.next
            head2.next = t1
            head = t1
            head2 = t2
```