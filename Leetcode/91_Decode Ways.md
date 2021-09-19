# 91. Decode Ways
Q: A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "111" can have each of its "1"s be mapped into 'A's to make "AAA", or it could be mapped to "11" and "1" ('K' and 'A' respectively) to make "KA". Note that "06" cannot be mapped into 'F' since "6" is different from "06".

Given a non-empty string num containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:
```
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```
Example 2:
```
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```
Example 3:
```
Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0. The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20".
Since there is no character, there are no valid ways to decode this since all digits need to be mapped.
```
Example 4:
```
Input: s = "1"
Output: 1
```

## Answer
首刷 300分鐘，Top-Down Recursion with memory (DP)版本
```python
# Runtime: 44 ms, faster than 5.02% of Python online submissions for Decode Ways.
# Memory Usage: 14.4 MB, less than 6.19% of Python online submissions for Decode Ways.
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """   
        size = len(s)
        mem = {}
        def ways(s1):
            if s1 == "0":
                return 0
            
            if s1 in mem:
                return mem[s1]
            
            lenS1 = len(s1)
            if lenS1 < 2:
                return 1
            
            w = 0
            for i in xrange(1, lenS1+1): # memorize !!!
                frontStr = s1[:i]
                rearStr = s1[i:]
                lenFront = len(frontStr)
                if lenFront > 2:
                    continue
                else:
                    intFrontStr = int(frontStr)
                    if (lenFront == 2 and (intFrontStr < 10 or intFrontStr > 26)) or intFrontStr == 0:
                        continue
                w += ways(rearStr)
            
            mem[s1] = w
            return w
            
        return ways(s)
```

首刷，無 DP 純 Top-Down Recursion版本 (Time exceeded)
```python
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """   
        size = len(s)
        
        def ways(s1):
            if s1 == "0":
                return 0
            
            lenS1 = len(s1)
            if lenS1 < 2:
                return 1
            
            w = 0
            for i in xrange(1, lenS1+1): # memorize !!!
                frontStr = s1[:i]
                rearStr = s1[i:]
                lenFront = len(frontStr)
                if lenFront > 2:
                    continue
                else:
                    intFrontStr = int(frontStr)
                    if (lenFront == 2 and (intFrontStr < 10 or intFrontStr > 26)) or int(frontStr) == 0:
                        continue
                w += ways(rearStr)
                
            return w
            
        return ways(s)
```

DP Recursive Bottom-Up (理解這解法較好，較易理解及實作)：\
[拮取自論譠最佳解](https://leetcode.com/problems/decode-ways/discuss/30358/Java-clean-DP-solution-with-explanation):
I used a dp array of size n + 1 to save subproblem solutions. dp[0] means an empty string will have one way to decode, dp[n] means the ways to decode a string of size n from start. I then check one digit and two digit combination and save the results along the way. In the end, dp[n] will be the end result

它的原理是 
> dp[n] means the ways to decode a string of size n from start.

所以 `dp[1]` 就是由左至右為一個字元長的排列組合數；`dp[2]`就是由左至右為兩個字元長的排列組合數。

那該如何獲得 `dp[n]`？
假設我們已知 `dp[1] ~ dp[k-1]` 該如何求得 `dp[k]`？我們可以推想，`dp[k]`的值可以拆解成兩個值 a 及 b 的和，即dp[k+1] = a + b，分別是將原本的字串 s，用最後一個字元及兩個字元來拆解：
* a 是 最後一個字元`s[k-1]` 跟 前面 `s[:k-1]`字串 的組合數，若最後一個字元可以被decode，那 a 就會等於 `1*dp[k-1]`，否則 a=0。
* b 是 最後兩個字元`s[k-2:k]` 跟 前面 `s[:k-2]`字串 的組合數，若最後兩個字元可以被decode，那 b 就會等於 `1*dp[k-2]`，否則 b=0。

所以遞迴原理
> dp[k] = ( dp[k-1] if s[k-1] can be decoded ) + ( dp[k-2] if s[k-2:k] can be decoded )

第一個括號中的 `s[k-1]` 代表最後一個字元，第二個括號中的 `s[k-2:k]` 代表最後兩個字元。

python:
```python
# Runtime: 8 ms, faster than 99.95% of Python online submissions for Decode Ways.
# Memory Usage: 13.7 MB, less than 31.93% of Python online submissions for Decode Ways.
class Solution(object):
    def numDecodings(self, s): 
        if s == "":
            return 0
        
        n = len(s)
        dp = [0]*(n+1)
        
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0
        
        for i in xrange(2, n+1):
            one = int(s[i-1: i])
            two = int(s[i-2: i])
            if one >= 1 and one <= 9:
                dp[i] += dp[i-1]
            if two >= 10 and two <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]
```

java:
```java
public class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0)
            return 0;
        
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = s.charAt(0) != '0' ? 1 : 0;
        for (int i = 2; i <= n; i++) {
            int first = Integer.valueOf(s.substring(i - 1, i));
            int second = Integer.valueOf(s.substring(i - 2, i));
            if (first >= 1 && first <= 9)
                dp[i] += dp[i-1];  
            
            if (second >= 10 && second <= 26)
                dp[i] += dp[i-2];
        }
        return dp[n];
    }
}
```