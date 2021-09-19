# 139. Word Break
Q: Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
* The same word in the dictionary may be reused multiple times in the segmentation.
* You may assume the dictionary does not contain duplicate words.
Example 1:
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```
Example 2:
```
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             
Note that you are allowed to reuse a dictionary word.
```
Example 3:
```
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

## Answer:
98分的解法，DP，觀念是 s這個字串會被拚接成功，**是因為一個個字組拚接起來的，前面拚出來才能拚下一個**，因此我們只要用一個布林陣列記錄有拚接起來的index，從true的 index 開始再去比較下一個字組，看看這字組能否拚接上去，將布林陣列記錄該位置 index 為true，如此反覆檢查字串s到最後一個字元，最後再檢查布林陣列的最後一個index若為 true，就代表s能拚接成功，下面為示意圖，注意此陣列第一個值為 true，這樣我們才能在迴圈裡一開始就做比較。請好好研究代碼的意義會比較容易懂。

這個布林陣列的概念，感覺跟排列組合裡的重覆組合有點關係。

這邊有個小技巧是python slicing的寫法超過index並不會跳error，只會回傳子陣列或子字串，如此寫法變得更精簡。

<img src="imgs\139_1.jpg" alt="drawing" width="300"/>

```python
"""
Solution-3: Dynamic Programming

Runtime: 24 ms, faster than 83.21% of Python online submissions for Word Break.
Memory Usage: 11.7 MB, less than 100.00% of Python online submissions for Word Break.
"""
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # [Opt] len is the Python's in-built function to count the length of an element.
        wordDict.sort(key=len)

        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True
        for i in xrange(N):
            if dp[i]:

                for word in wordDict:
                    len_w = len(word)    
              
                    # [Opt] 這邊也可以再為一些特殊情形做一點改善(但總體而言不一定快)，
                    # 將 wordDict先做sort，如果 i + len(wordDict[0])
                    # 超過 s 的index，那 wordDict的迴圈就可以提早結束
                    if i + len_w > N:
                        break
                        
                    # 小技巧：list或字串的 slicing 若超過範圍不會跳錯
                    if s[i: i+len_w] == word:
                        dp[i+len_w] = True
        return dp[-1]
```

60分的解法
```python
"""
Solution-0: BF Recursion (Brute force, timeout)
"""
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def helper(s, curr_idx):
                        
            if curr_idx == len(s) :
                return True
            
            N = len(s)
            
            for word in wordDict:

                # 若想將不同的statement斷行，可以在最外層加括號
                if (
                    len(word) <= N - curr_idx and 
                    s[curr_idx: curr_idx + len(word)] == word and 
                    helper(s, curr_idx + len(word))
                ):
                    return True
            
            return False
        
        return helper(s, 0)
```

93分的解法 (前面60分解法的改善延伸)\
2刷(較好懂):

```python
class Solution:
    def wordBreak(self, string, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        size = len(string)
        falseSet = set()
        
        def dfs(s):
            if s==string:
                return True

            if s in falseSet:
                return False
            
            for word in wordDict:
                s2 = s+word
                if len(s2) <= size:
                    if string.find(s2) == 0:
                        if dfs(s2):
                            return True
            # Why falseSet can be faster ?
            # If "a", "aa", "aaa" are members of WordDict.
            # "a" can make "aa", "aaa" and so forth. If they make dfs() return False, they'd be added into falseSet. So next time the "aa" from WordDict goes into the dfs(), the falseSet check can return False earlier.
            falseSet.add(s)
            return False
        
        return dfs("")
```
高手解(較難懂)
```python
"""
Solution-1: Recursion with memory

Runtime: 12 ms, faster than 99.77% of Python online submissions for Word Break.
Memory Usage: 12 MB, less than 44.68% of Python online submissions for Word Break.

Runtime: 20 ms, faster than 94.07% of Python online submissions for Word Break.
Memory Usage: 11.7 MB, less than 97.87% of Python online submissions for Word Break.
"""
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        falseSet = set()
        N = len(s)

        def helper(s, curr_idx):
                        
            if curr_idx in falseSet:
                return False
            
            if curr_idx == N:
                return True
            
            for word in wordDict:
                                
                len_w = len(word)
                if (
                    len_w <= N - curr_idx and 
                    s[curr_idx: curr_idx + len_w] == word and 
                    helper(s, curr_idx + len_w)
                    ):
                    return True
            
            falseSet.add(curr_idx)
            return False
            
        return helper(s, 0)    
```

## Review
3刷 (約24分)

```python
# Runtime: 32 ms, faster than 94.09% of Python3 online submissions for Word Break.
# Memory Usage: 14.3 MB, less than 89.23% of Python3 online submissions for Word Break.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        size = len(s)
        dp = [False]*(size+1)
        words = wordDict
        words.sort(key=len)
        dp[0] = True
        
        for i in range(size+1):
            if dp[i]:
                
                for w in words:
                    size2 = len(w)
                    if i+size2 < size+1 and s[i: i+size2] == w:
                        dp[i+size2] = True
                    
        return dp[-1]
```