# 516. Longest Palindromic Subsequence
Q: Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
```
Input:
"bbbab"
```
```
Output:
4
```
One possible longest palindromic subsequence is "bbbb".
 
Example 2:

```
Input:
"cbbd"
```
```
Output:
2
```
One possible longest palindromic subsequence is "bb".

## Answer
印度youtuber觀念講的滿不錯的: https://www.youtube.com/watch?v=_nCsPn7_OgI

Jeff看解後一刷: 46分 (遞迴法，比較容易寫得出來)
Runtime: 876 ms, faster than 92.14% of Python online submissions for Longest Palindromic Subsequence.
Memory Usage: 81.2 MB, less than 12.14% of Python online submissions for Longest Palindromic Subsequence.

```python
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        dp = [[0]*size for _ in xrange(size)]
        
        def getLongest(start, end):
            if start > end:
                return 0
            elif start == end:
                dp[start][end] = 1
                return 1
            elif dp[start][end] > 0:
                return dp[start][end]
            
            lmax = 0
            if s[start]==s[end]:
                lmax = getLongest(start+1, end-1) + 2
            else:
                lmax = max(getLongest(start, end-1), getLongest(start+1, end))
            dp[start][end] = lmax
            return lmax
        
        return getLongest(0, size-1)
```

還有迭代的寫法滿有趣的，是參考論譠的java解，注意它的兩個迴圈，第一個是從最右開始往左移動，然後本身往右邊擴張，如此會讓迴圈裡巡彷的邏輯變得相當簡潔
```java
public class Solution {
    public int longestPalindromeSubseq(String s) {
        int[][] dp = new int[s.length()][s.length()];
        
        for (int i = s.length() - 1; i >= 0; i--) {
            dp[i][i] = 1;
            for (int j = i+1; j < s.length(); j++) {
                if (s.charAt(i) == s.charAt(j))
                    dp[i][j] = dp[i+1][j-1] + 2;
                else
                    dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1]);
            }
        }
        return dp[0][s.length()-1];
    }
}
```