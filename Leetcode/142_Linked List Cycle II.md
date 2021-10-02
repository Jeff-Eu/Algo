# 142. Linked List Cycle II
Q: Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Example 1:

```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```
Example 2:

```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```
Example 3:

```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
``` 

## Answer
141 Linked List Cycle 是 Floy's龜兔演算法基本型；而這題是進階型。
關於該演算法的解說，請參考 [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) 的 markdown file

2021/10/2刷，約45分 包含導公式，以及卡在下面的trap#1
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next) or (not head.next.next):
            return None
        
        slw = head.next
        fst = head.next.next

''' trap#1: 錯誤寫法造成無窮迴圈，fst要從自己的fst開始才是最新的，不能從slw設給它，否則會變成跟之前一樣      
        while slw != fst:
            slw = slw.next
            if slw and slw.next:
                fst = slw.next
            else:
                return None
'''
        # 解決 trap#1 的正確解法
        while slw != fst:
            slw = slw.next
            if fst.next and fst.next.next:
                fst = fst.next.next
            else:
                return None

        slw = head
        while slw != fst:
            slw = slw.next
            fst = fst.next
            
        return slw
```

2刷，10分
```python 3
# Runtime: 44 ms, faster than 94.26% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 17.3 MB, less than 25.64% of Python3 online submissions for Linked List Cycle II.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        slw = head
        fst = head
        
        while fst and fst.next:
            fst = fst.next.next
            slw = slw.next
            if fst == slw:
                break
                
        if not fst or not fst.next:
            return None
        
        slw = head
        
        while slw != fst:
            slw = slw.next
            fst = fst.next
        
        return slw
```

```java kotlin
// Runtime: 108 ms, faster than 58.24% of Kotlin online submissions for Linked List Cycle II.
// Memory Usage: 34.6 MB, less than 16.48% of Kotlin online submissions for Linked List Cycle II.
/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun detectCycle(head: ListNode?): ListNode? {
        
        if(head == null || head.next == null)
            return null
        
        var fst = head!!
        var slw = head!!

        do {
            if(fst.next != null && fst.next.next != null)
                fst = fst.next.next
            else
                return null
            
            slw = slw.next
        }while(slw != fst)
        
        slw = head
        while(slw != fst) {
            
            fst = fst.next
            slw = slw.next
        }
        return fst
    }
}
```

#medium