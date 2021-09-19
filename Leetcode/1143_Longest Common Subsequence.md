# 1143. Longest Common Subsequence
Q: Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:
```
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
```
Example 2:
```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```
Example 3:
```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
``` 

## Answer

題目跟 583大同小異，請參考 583詳解的 Method 3解法
```python
# Runtime: 320 ms, faster than 93.68% of Python online submissions for Longest Common Subsequence.
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        len1 = len(text1)+1
        len2 = len(text2)+1
        
        # Initializing 2D array, memorize it !
        arr = [[0]*len2 for _ in xrange(len1)]
        
        for i in xrange(1, len1):
            for j in xrange(1, len2):
                if text1[i-1] == text2[j-1]:
                    arr[i][j] = 1 + arr[i-1][j-1]
                else:
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1])
                    
        return arr[len1-1][len2-1]                    
```
