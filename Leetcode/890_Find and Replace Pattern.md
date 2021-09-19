# 890. Find and Replace Pattern
Q: You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

Example 1:
```
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
``` 

Note:

* 1 <= words.length <= 50
* 1 <= pattern.length = words[i].length <= 20

## Answer
Jeff純二刷 (約25分):

需注意為了要1對1 mapping，所以用額外一個set去儲存target值
```python
#Runtime: 20 ms, faster than 75.65% of Python online submissions for Find and Replace Pattern.
#Memory Usage: 13.4 MB, less than 93.04% of Python online submissions for Find and Replace Pattern.
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        size =len(pattern)
        out=[]
        for word in words:
            dic={}
            sett=set()
            if len(word) != size:
                continue
                
            for i in xrange(size):
                c = pattern[i]
                c2 = word[i]
                if c not in dic:
                    if c2 not in sett:
                        dic[c] = c2
                        sett.add(c2)
                    else:
                        break
                elif dic[c] != word[i]:
                    break

                if i==size-1:
                    out.append(word)

        return out
```

看解答後一刷:
看 Leetcode 詳解的Two Map方法就好，雖然One Map的方法沒看懂，但兩種方法的時空複雜度相同。
```python
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        N = len(pattern)
        r = []

        for w in words:
            m1 = {}
            m2 = {}        
            isPass = True
            for c1, c2 in zip(w, pattern):
                if c1 not in m1:
                    m1[c1] = c2
                if c2 not in m2:
                    m2[c2] = c1

                if not (m1[c1] == c2 and m2[c2] == c1):
                    isPass = False
                    
            if isPass:
                r.append(w)
                    
        return r
```