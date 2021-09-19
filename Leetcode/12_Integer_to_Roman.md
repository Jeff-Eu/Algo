# 12. Integer to Roman
Q: Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:
```
Input: num = 3
Output: "III"
```
Example 2:
```
Input: num = 4
Output: "IV"
```
Example 3:
```
Input: num = 9
Output: "IX"
```
Example 4:
```
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
```
Example 5:
```
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```
## Answer
二刷，約27分

Time: O(N) where N is the digits numbers.

```python 3
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10]
```


```python 3
class Solution:
    def intToRoman(self, num: int) -> str:
        
        ls = ["I","V","X","L","C","D","M"]
        d = 1000 # divisor
        ans = ""
        i = len(ls)-1
        while num != 0:
            m = num // d # m is quotient
            if m==9:
                ans += ls[i] + ls[i+2] 
            elif m==4:
                ans += ls[i] + ls[i+1]
            elif m>0:
                if m < 4: # 1 2 3
                    ans += ls[i]*m
                else: # 5 6 7 8
                    ans += ls[i+1]
                    ans += ls[i]*(m-5)
            i-=2  # 注意我這是寫往前跳兩格
            num %= d
            d //= 10
            
        return ans
```
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4e8e0b04-18e3-41fc-8c7d-6acc37f3efe0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210318T035800Z&X-Amz-Expires=86400&X-Amz-Signature=7f40f433a6bbd1d6f0dfbbe4420c4f77cd58d05bf0692f7d1e19643748f98a94&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

## Archived
Jeff's answer:

**Concept**: 
- Divide Roman number from largest one to smallest one.
- Subtract the each Roman number from the original integer.
- Deal exclusively with the digit which is 4x10^n or 9x10^n, where n is a natural number. Because only they can be described as minus form of Roman number.

**Python note**
- Logarithm function returns a float number, not integer. As [python math function doc said](https://docs.python.org/2/library/math.html), *"The following functions are provided by this module. Except when explicitly noted otherwise, all return values are **floats**."*. 

```python
from math import log10
class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        
        nums = [1000, 500, 100, 50, 10, 5, 1]
        strs = ["M", "D", "C", "L", "X", "V", "I"]

        out = ""
        i = 0
        while A > 0:
            n = A / nums[i]
            if n > 0:
                A -= n * nums[i]
                out += n * strs[i]

            g10 = log10(nums[i])
            g10int = int(g10)

            # Deal with the digit which is 9*10^n
            if nums[i] >= 10 and g10 == g10int:
                f = 10 ** (g10int - 1) # 比"除", nums[i] / 10 還有效率
                if (A + f) / nums[i] > 0:
                    out += strs[i+2] + strs[i]
                    A %= f
            # Deal with the digit which is 4*10^n
            elif i + 1 <= len(nums) and nums[i] >= 5:
                if A != nums[i+1] and (A + nums[i+1]) / nums[i] > 0:
                    out += strs[i+1] + strs[i]
                    A %= nums[i+1]
            i += 1

        return out
```


論譠別人的解(有點暴力)：
```python
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10]
```