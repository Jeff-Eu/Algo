# 5. Longest Palindromic Substring
Q: Given a string s, return the longest palindromic substring in s.

 

Example 1:
```
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```
Example 2:
```
Input: s = "cbbd"
Output: "bb"
```
Example 3:
```
Input: s = "a"
Output: "a"
```
Example 4:
```
Input: s = "ac"
Output: "a"
```

## Answer
看過再複刷:
```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        mxNum = 0
        sz = len(s)
        
        def getMaxPalAt(lt, rt):
            out = ""
            while lt >=0 and rt < sz:
                if s[lt] == s[rt]:
                    out = s[lt:rt+1]
                    lt -= 1
                    rt += 1
                else:
                    break
            return out
        
        for i in xrange(sz):
            ans = max(getMaxPalAt(i, i), ans, key=len) # 套用了這裡的 key=len之後，會回傳前面參數裡 len最大的參數
            
        for i in xrange(sz-1):
            ans = max(getMaxPalAt(i, i+1), ans, key=len)
            
        return ans
```
修改上面再復刷如下，代碼有點醜，不適合考試
```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 注意下兩行，是如何 初始化 global變數，來給 nest function使用，請參見 [UnboundLocalError with nested function scopes](https://stackoverflow.com/questions/2609518/unboundlocalerror-with-nested-function-scopes/2609593#2609593)
        ans = [""]
        amxLen = [0]
        
        sz = len(s)
        
        def getMaxPalAt(lt, rt):
            if lt == rt:
                llen = 1 # llen is local length for s[lt:rt+1]
            else:
                if s[lt] == s[rt]:
                    llen = 2
                else:
                    llen = 0
            out = ""
            while lt >=0 and rt < sz:
                if s[lt] == s[rt]:
                    if llen > amxLen[0]:
                        amxLen[0] = llen
                        ans[0] = s[lt:rt+1]
                    lt -= 1
                    rt += 1
                    llen += 2
                else:
                    break
        
        for i in xrange(sz):
            getMaxPalAt(i, i)
            
        for i in xrange(sz-1):
            getMaxPalAt(i, i+1)
            
        return ans[0]
```
---------
複刷：目前較好理解跟實作出來的作法，用到 647. Palindromic Substrings 的函式技巧

python
```python
# Runtime: 1348 ms, faster than 43.18% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14.4 MB, less than 63.02% of Python3 online submissions for Longest Palindromic Substring.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        size = len(s)
        def getPal(l, r):
            out=""
            while l>=0 and r<size and s[l]==s[r]:
                out = s[l:r+1]
                l-=1
                r+=1
            return out
        
        ans = ""
        for i in range(size):
            ans = max(ans, getPal(i,i), getPal(i,i+1), key=len)
        return ans
```

java
```java
// Runtime: 24 ms, faster than 80.08% of Java online submissions for Longest Palindromic Substring.
// Memory Usage: 39.1 MB, less than 69.67% of Java online submissions for Longest Palindromic Substring.
class Solution {
    public String longestPalindrome(String s) {
        
        String[] r = {""};
        int size = s.length();
        for(int i=0; i<size; i++){
            longestPalinFrom(i, i, s, r);
        }
        
        for(int i=0; i<size-1; i++){
            longestPalinFrom(i, i+1, s, r);
        }
        return r[0];
    }
    
    void longestPalinFrom(int l, int r, String s, String[] out) {
        
        int size = s.length();
        int mxSize = out[0].length();
        while(l>=0 && r<size && s.charAt(l)==s.charAt(r)) {
            
            int newSize = r-l+1;
            if(newSize > mxSize) {
                out[0] = s.substring(l, r+1);
                mxSize = newSize;
            }
            l-=1;
            r+=1;
        }
    }
}
```

## Archived
題目示意看這影片的介紹
https://www.youtube.com/watch?v=fV-TF4OvZpk

解答請看官網詳解的gif跟我用python寫的程式碼
```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        out=""
        size = len(s)
        def getStr(left, right):
            while left>=0 and right<size and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1: right]
            
            
        for i in xrange(size):
            out = max(getStr(i, i), getStr(i, i+1), out, key=len)
            
        return out
```
以下Lemma皆可適用於java跟python，Skill僅適用於python

**Lemma1**：(從詳解中的java solution學來的)，在array中某個index i 會使得 i 加上某個長度L等於index j，亦即 i + L == j，那 j - L == i
```
array:  0 1 2 3 4 5 6 7 
          i <-- L -->
                    j
```
**Lemma2**:
若 L 為奇數，則 L/2 == (L-1)/2；若 L 為偶數，則 (L-1)/2 == L/2 - 1


**Theorem**：(從詳解中的java solution推理而來的)

如下圖，陣列中有一段長度是 L 的子陣列，定義i為：若L為奇數，i就是子陣列的中心位置，
若L為偶數，i會是子陣列中間偏左一位的位置，則該子陣列的起始位置 s 跟結束位置 e 分別為下式，可由 lemma1 跟 lemma2 證明而得到：
```
s = i - (L-1)/2
e = i + L/2

   <------ L ------> 
 0 0 0 0 0 0 0 0 0 0 0 0 0 0
   s       i       e
```
Skill: key=len  例如 sort(s, key=len)   或像是   max(s1, s2, s3, s4, key=len)
