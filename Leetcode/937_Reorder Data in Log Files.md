# 937. Reorder Data in Log Files
Q: You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

Example 1:
```
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
```
Example 2:
```
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
```

## Answer
首刷，約26分。

這題不難，只是要對語法熟悉。

```python
# Runtime: 20 ms, faster than 93.13% of Python online submissions for Reorder Data in Log Files.
# Memory Usage: 13.7 MB, less than 83.28% of Python online submissions for Reorder Data in Log Files.
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letterlogs = []
        digitlogs = []
        
        for log in logs:
            if log[-1].isalpha():  # 要懂 string.isalpha()
                letterlogs.append(LetterLog(log))
            else:
                digitlogs.append(log)
                
        letterlogs.sort()
        
        letterStrs = []
        for lg in letterlogs:
            letterStrs.append(lg.log)
            
        return letterStrs + digitlogs
                
class LetterLog(): # 要熟 comparator 的寫法
    def __init__(self, log):
        self.log = log
        idx = log.index(" ")
        self.id = log[:idx]
        self.content = log[idx:]
    def __lt__(self, other):  # lt 跟 eq 都是回傳 boolean
        if self.content == other.content:
            return self.id < other.id
        else:
            return self.content < other.content
        
    def __eq__(self, other):
        return self.log == other.log
```