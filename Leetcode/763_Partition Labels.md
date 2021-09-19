# 763. Partition Labels
Q: A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
```
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
``` 

Note:
```
S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
```
## Answer
Jeff's first
```python
# Runtime: 52 ms, faster than 11.07% of Python online submissions for Partition Labels.
# Memory Usage: 13.7 MB, less than 15.95% of Python online submissions for Partition Labels.
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        s = 0 # start
        size = len(S)
        indexArr = []

        while s < size:
            checkSet = set()
            buffSet= set()
            checkSet.add(S[s])
            for i in xrange(s+1, size):
                if S[i] in checkSet:
                    for item in buffSet:
                        checkSet.add(item)
                    buffSet = set()
                    s = i
                else:
                    buffSet.add(S[i])

            indexArr.append(s)
            s+=1
                
        out=[]
        lastIdx = -1
        for item in indexArr:
            out.append(item-lastIdx)
            lastIdx=item
            
        return out
```

詳解的解:
```python
# Runtime: 20 ms, faster than 97.49% of Python online submissions for Partition Labels.
# Memory Usage: 13.6 MB, less than 38.74% of Python online submissions for Partition Labels.
class Solution(object):
    def partitionLabels(self, S):
        # The "last" is a dictionary which updates the value on the same key.
        last = {c: i for i, c in enumerate(S)}
        print last
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans
```