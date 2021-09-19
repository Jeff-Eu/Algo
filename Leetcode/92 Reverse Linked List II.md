# 92. Reverse Linked List II

Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return *the reversed list*.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg](https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg)

```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```

**Example 2:**

```
Input: head = [5], left = 1, right = 1
Output: [5]
```

**Constraints:**

- The number of nodes in the list is `n`.
- `1 <= n <= 500`
- `500 <= Node.val <= 500`
- `1 <= left <= right <= n`

**Follow up:**

Could you do it in one pass?

## Answer

拔除插入法(詳見206)：目前最簡潔易懂的解法，但並非最快解，原因是每次 pre.next = tmp 如果可以簡化成 subHead = tmp 會更快一點，最後只要再做 pre.next = subHead 把全部串列接起來(這是大概的想法)。

記憶：

- 首先，writing down an example or drawing is a good habit ！這同時也能增加撰寫的速度及正確性。
- 額外宣告的變數包含：
    - 第二個迴圈只用到三個額外變數，prev, curr, tmp
    - 最後回傳需要的 dummy 變數(複製出pre)；回傳 head 是錯的，因為 head(第一個) 被拔除的話，head就不會指向list的第一個了。

```python
# Runtime: 16 ms, faster than 86.87% of Python online submissions for Reverse Linked List II.
# Memory Usage: 13.6 MB, less than 62.76% of Python online submissions for Reverse Linked List II.
class Solution(object):
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        
        pre = dummy
        curr = head  # For better explaination
        for _ in xrange(m - 1): # move forward (m-1) steps
            pre = pre.next
        
        curr = pre.next
        
        # reverse m to n
        for _ in xrange(n - m):
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp

        return dummy.next
```

二刷後複習時，發現到快速記法！注意下面這段常會寫錯的code：

```python
# reverse m to n
for _ in xrange(n - m):
    tmp = curr.next
    curr.next = tmp.next
    tmp.next = pre.next
    pre.next = tmp
```

首先寫出 `tmp = curr.next` 是比較容易的，接下只要照下面"梳子圖"的對映關係就可以容易寫出剩下的值：

![92%20Reverse%20Linked%20List%20II%20d7fca70c52b24a30af6dd2c57923964c/92_1.png](92%20Reverse%20Linked%20List%20II%20d7fca70c52b24a30af6dd2c57923964c/92_1.png)

為什麼會有這種神奇的巧合？證明很簡單，因為這是在 Linked List 上的一種**拔除再插入**的操作，這樣的操作結束後**不會造成任何一個 node 同時被兩個 nodes 所指向**，也就是說每個node只被一個node所指向 (不像刪除結點那樣，因為被刪除的結點(令B)沒人指到它，在具有Garbage collection的語言中它就可以自動被回收，B就會消失，但如果在不具垃圾回收的語言中，例如C/C++，因為B還是存在，而它會指向某個結點A，造成實際上A會有兩個node指向它，除非你將B給 delete掉)；因此，以上圖任一行來說，例如 `curr.next = tmp.next`就代表 `curr.next` 所指向的跟 `tmp.next`是一樣的，這樣會造成 tmp.next 所指向的被兩個 node 所指向，因此下一行才不得不去設定 `tmp.next` 的新值，同理亦可說明其他行。

上面這個關係在 206 Reverse Linked List (這題的簡化版) 也完全適用。

Kotlin複刷:

```kotlin
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
    fun reverseBetween(head: ListNode?, m: Int, n: Int): ListNode? {
        var pre = ListNode(0)
        pre.next = head
        var pre2 = pre
        
        var curr = head!!
        for(i in 1..m-1) {
            pre = pre.next!!
            curr = curr.next!!
        }
        
        for (i in 1..n-m) {
            var tmp = curr.next!!
            curr.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        }
        
        return pre2.next
    }
}
```

java複刷

```java
// Runtime: 0 ms, faster than 100.00% of Java online submissions for Reverse Linked List II.
// Memory Usage: 36.5 MB, less than 67.87% of Java online submissions for Reverse Linked List II.
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
    public ListNode reverseBetween(ListNode head, int m, int n) {
        
        ListNode prev = new ListNode(0);
        prev.next = head;
        ListNode curr = head;
        ListNode prev2 = prev;
        
        for(int i=0; i<m-1; i++) {
            prev = prev.next;
            curr = curr.next;        
        }
        
        /* writing down an example or drawing is a good habit 
        1 2 3 4
        p c
        1 3 2 4
        p   c
        */
        for(int i=0; i<(n-m); i++) {
            ListNode tmp = curr.next;
            curr.next = tmp.next;
            tmp.next = prev.next;
            prev.next = tmp;
        }
        
        return prev2.next;
    }
}
```

C複刷 (戰勝100%)

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseBetween(struct ListNode* head, int left, int right){
    struct ListNode *dummy = malloc(sizeof(struct ListNode));
    dummy->next = head;
    
    struct ListNode *pre = dummy;
    struct ListNode *curr = head;
    for(int i=0; i<left-1; i++) {
        pre = pre->next;
    }
    curr = pre->next;
    
    int range = right-left;
    for(int i=0; i<range; i++) {
        struct ListNode *tmp = curr->next;
        curr->next = tmp->next;
        tmp->next = pre->next;
        pre->next = tmp;
    }
    
    struct ListNode *ans = dummy->next;
    free(dummy);
    return ans;
}
```