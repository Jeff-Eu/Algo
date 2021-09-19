# 234. Palindrome Linked List

Given the `head` of a singly linked list, return `true` if it is a palindrome.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)

```
Input: head = [1,2,2,1]
Output: true
```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg](https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg)

```
Input: head = [1,2]
Output: false
```

**Constraints:**

- The number of nodes in the list is in the range `[1, 10^5]`.
- `0 <= Node.val <= 9`

**Follow up:**

Could you do it in O(n) time and O(1) space?

## Answer

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
    public boolean isPalindrome(ListNode head) {
        ListNode curr = head;
        int sz = 0;
				// 先循訪一遍，看 list 是多長
        while(curr!=null) {
            sz++;
            curr = curr.next;
        }
				// 只有一個元素，直接回傳 true
        if(sz==1)
            return true;
        
				// 接下來為了要找出後半部的第一個位置，
				// 再一次從頭往前走一半的距離，
				// 找到之後將它存入一個變數稱作second
        curr = head;
        for(int i=0; i<sz/2; i++)
            curr = curr.next;
        
				// 這邊要特別注意若長度是奇數，要再往前多走一步
        if(sz%2==1)
            curr = curr.next;
        
        ListNode second = curr;

				// 開始反轉前半部
        curr = head;
        // reverse the first half
        for(int i=0; i<sz/2-1; i++) {
            ListNode tmp = curr.next;
            curr.next = tmp.next;
            tmp.next = head;
            head = tmp;
        }
        
				// 最後比較前半部與後半部的元素值是否皆相同
        for(int i=0; i<sz/2; i++) {
            if(second.val != head.val)
                return false;
            
            head = head.next;
            second = second.next;
        }
        return true;
    }
}
```

Time: O(n), Space: O(1)