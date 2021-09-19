# 206. Reverse Linked List

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

```
Input: head = [1,2]
Output: [2,1]
```

**Example 3:**

```
Input: head = []
Output: []
```

**Constraints:**

- The number of nodes in the list is the range `[0, 5000]`.
- `5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

## Answer

Jeff三刷(拔插法) (剛好最簡潔)

記憶，這裡只用到兩個額外變數，curr, tmp

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        # 注意！不能沒有 curr，而將 head 當作 curr 用，否則回傳的會是 list 的 tail
        curr = head
        while curr.next:
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = head
            head = tmp
            
        return head
```

解一，拔插法：簡化 92. Reverse Linked List II 的解 (以後用這種解就可以同時吃兩題) Iterative法，跟解四用到的技巧有點像，都會有一個變數(在這裡就是 curr)永遠指向的是範圍內最後一個list item，但curr不會變，只有curr.next 的值有改變。

記憶，這裡只用到三個額外變數，prev, curr, tmp

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = ListNode(0, None)
        prev.next = head
        curr = head  # For better explaination
        if not curr:
            return curr
        
        # note that curr is NEVER set !!
        while curr.next:
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
        
        return prev.next
```

k = n 情況: p>3>2>1>4>5>6 ===> 每一次疊代就把 c (current) 指向的值(curr.next)移到最前面 c

k = 1 情況: p>1>2>3>4>5 c

```c
// Definition for singly-linked list.
 struct ListNode {
     int val;
     struct ListNode *next;
 };

struct ListNode* reverseList(struct ListNode* head){

    struct ListNode* pre = malloc(sizeof(struct ListNode));
    struct ListNode* curr = head; // rename
    pre->next = curr;

    if(head == NULL)
        return head;
    
    while(curr->next != NULL) {
        struct ListNode* tmp = curr->next;
        curr->next = tmp->next;
        tmp->next = pre->next;
        pre->next = tmp;
    }
    head = pre->next;
    free(pre);
    return head;
};

/*

12345
^
c

043215
p   c

*/
```

解二: Jeff，不太正規的 Recursive法，把 Recursive當作 Iterative用XD ：

```python
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = ListNode(0, None)
        prev.next = head
        if not head:
            return head
        
        def toFirst():
            if head.next:
                tmp = head.next
                head.next = tmp.next
                tmp.next = prev.next
                prev.next = tmp
                toFirst()
            
        toFirst()
            
        return prev.next
```

解三(詳解提供的)，依次反向法:

非解一的拔插法，但也很有意思，可以畫圖就知道它的動態行為是什麼，所以我稱之為依次反向法。這方法會比拔插法快(因為 `.` 用的比較少)

```python
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
```

解四： Runtime: 20 ms, faster than 93.79% of Python online submissions for Reverse Linked List. Memory Usage: 14.7 MB, less than 92.15% of Python online submissions for Reverse Linked List.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        prev = head
        curr = head.next
        
        while curr:
            prev.next = curr.next
            curr.next = head
            head = curr
            curr = prev.next

        return head
```

解四explain: k = n 情況

3>2>1>4>5>6 ===> 每一次疊代就把 c (current) 指向的值移到最前面 h p c

k = 1 情況

1>2>3>4>5 h c p