# 14. Longest Common Prefix
Q: Write a function to find the longest common prefix string amongst an array of strings.

# Answer
Jeff's answer
```python
class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):

        i = 0
        while i < len(A[0]):

            c = A[0][i]
            
            for s in A[1:]:
                
                if len(s) <= i or c != s[i]:
                    if i > 0:
                        return A[0][0:i]
                    else:
                        return ""
            
            i += 1
            
        return A[0][0:i]
```