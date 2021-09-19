# LeetCode 21. Merge Two Sorted Lists

## 思路
學平's
* 先創一個新的節點result
* l1, l2比較目前節點的數值, 若l1.val < l2.val 則將l1目前節點加到result, l1指向下一節點 (l2.val < l1.val 同理), 直到l1或l2變成null為止。
* 最後將 l1,l2剩下的節點加到result

Jeff's
* 這跟華碩部門間彼此打考績的方法一樣！

## Answer
* 以圖像表示 p 被assign的值與 p.next，常都會使用箭頭，但這會使人混淆，
* 所以現在開始定義只有 p.next 可以使用箭頭，assign的話就寫在下面，例如
```
b=a
p.next = a
的圖為
p->a
   b 
```
如果這時 b=c ，圖就會變成
```
p->a    c
        b
```
可看到b與a已完全斷線無關了\
首先介紹錯誤的陷阱寫法:
```python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        p=l1
        q=l2
        pre=ListNode()
        head=None
        pre.next=head
        while p and q:
            if p.val < q.val:
                head=p
                p=p.next
            else:
                head=q
                q=q.next
            head=head.next
            
        while p:
            head=p
            p=p.next
            head=head.next
        
        while q:
            head=q
            q=q.next
            head=head.next
            
        return pre.next
```      

正確寫法:\
Jeff二刷
Runtime: 20 ms, faster than 92.61% of Python online submissions for Merge Two Sorted Lists.
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p=l1
        q=l2
        pre=ListNode()
        pre2=pre
        while p and q:
            if p.val < q.val:
                pre.next=p
                p=p.next
            else:
                pre.next=q
                q=q.next
            pre=pre.next
            
        # while p:
        #     pre.next=p
        #     p=p.next
        #     pre=pre.next
        
        # while q:
        #     pre.next=q
        #     q=q.next
        #     pre=pre.next
            
        # 上面註解的可改良成下面，否則只能打敗 74% 左右
        if p:
            pre.next=p
        if q:
            pre.next=q

        return pre2.next
```

Jeff's 一刷
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        lr = lp = ListNode(0)
        
        while l1 or l2 :
            
            if l1 and not l2:
                lp.next = ListNode(l1.val)
                l1 = l1.next
            elif l2 and not l1:
                lp.next = ListNode(l2.val)
                l2 = l2.next
            elif l1.val > l2.val:
                lp.next = ListNode(l2.val)
                l2 = l2.next
            else:
                lp.next = ListNode(l1.val)
                l1 = l1.next
                
            lp = lp.next
            
        return lr.next
```
學平's
```javascript
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    var result = new ListNode(0);
    
    var current = result;
    
    while(l1 !== null && l2 !== null) {
        
        // l1, l2 較小的數加入result
        if (l1.val < l2.val) {
            current.next = l1;
            l1 = l1.next;
        } else {
            current.next = l2;
            l2 = l2.next;
        }
        current = current.next;
    }
    
    
    //l1, l2剩下的Node 加到 result
    if (l1 !== null) {
        current.next = l1;
    }
    
    if (l2 !== null) {
        current.next = l2;
    }
    
    return result.next;
};
```