# 424. Longest Repeating Character Replacement
Q: Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:
```
Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
``` 

Example 2:
```
Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```
## Answer
[力扣高手有詳細的介紹如何使用移動視窗解題](https://leetcode-cn.com/problems/longest-repeating-character-replacement/solution/tong-guo-ci-ti-liao-jie-yi-xia-shi-yao-shi-hua-don/)

解題思路：想像最後得到的連續同字母字串一定會被一個長度會 M 的 window 給包住，在這 window 中，那些變換前的字母就 P 個，那同一字母的就有 L = M - P，這 L 就會是這移動 window 從最左邊移到最右邊過程中， window 內有最多同字母的數量。

```python
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        
        size = len(s)
        table = [0]*26
        left = 0
        maxV = 0
        for right in xrange(0, size):
            idx = ord(s[right]) - ord('A')
            table[idx] += 1
            maxV = max(maxV, table[idx])
            if right-left+1 > maxV+k:
                table[ord(s[left]) - ord('A')] -= 1
                left += 1
                
        return size - left
```
