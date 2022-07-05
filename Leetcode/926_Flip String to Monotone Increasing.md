# 926. Flip String to Monotone Increasing
A binary string is monotone increasing if it consists of some number of `0`'s (possibly none), followed by some number of `1`'s (also possibly none).

You are given a binary string `s`. You can flip `s[i]` changing it from `0` to `1` or from `1` to `0`.

Return _the minimum number of flips to make_ `s` _monotone increasing_.

**Example 1:**

**Input:** s = "00110"
**Output:** 1
**Explanation:** We flip the last digit to get 00111.

**Example 2:**

**Input:** s = "010110"
**Output:** 2
**Explanation:** We flip to get 011111, or alternatively 000111.

**Example 3:**

**Input:** s = "00011000"
**Output:** 2
**Explanation:** We flip to get 00000000.

**Constraints:**

-   `1 <= s.length <= 105`
-   `s[i]` is either `'0'` or `'1'`.

## Answer

I figured out the solution (almost optimum) without any hint, but I spent separate time (by 2~3 different days) to list some examples and observed some rules. This method can improved to better by avoiding the `ls` but would be harder to realise.
```python
class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        sz = len(s)
            
        ls = []
        v = '0'
        c = 0
        for i in xrange(sz):
            if s[i] == v:
                c += 1
            else:
                if v == '1':
                    v = '0'
                else:
                    v = '1'
                ls.append(c)
                c = 1
        ls.append(c)
        
        szNum = len(ls)
        currSum = 0        
        for i in xrange(szNum):
            if i%2==0:
                currSum += ls[i]
        
        mi = currSum
        for i in xrange(szNum):
            if i%2 == 0:
                currSum -= ls[i]
                mi = min(currSum, mi)
            else:
                currSum += ls[i] 
            
        return mi

'''
Example for figuring out the solution:

0001111000001111111001111000
=>
0 1 0 1 0 1 0
3 4 5 7 2 4 3

x 4 x 7 x 4 x  v
x 4 x 7 x 4 3  
x 4 x 7 x x 3  v
x 4 x 7 2 x 3
x 4 x x 2 x 3  v
x 4 5 x 2 x 3
x x 5 x 2 x 3  v
3 x 5 x 2 x 3

// The filter below uses more complicated computation in code, so just ignore it.
x 4 x 7 x 4 x  v
x 4 x 7 x x 3  v
x 4 x x 2 x 3  v
x x 5 x 2 x 3  v
'''
```