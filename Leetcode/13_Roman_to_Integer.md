# 13. Roman to Integer
Q: Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Read more details about roman numerals at [Roman Numeric System](https://zh.wikipedia.org/zh-tw/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97)

## Answer
二刷，約 21分，一送即過，多虧題目有給些不錯的範例，記得解這題反轉(第12題，稍難一點)，這種題目不難，因為：
* Roman numerals are usually written largest to smallest from left to right. 
* 不用考慮進位的問題

```python 3
class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        nxt = "I"
        ans = 0
        for c in reversed(s):
            if mp[c] >= mp[nxt]:
                ans += mp[c]
                nxt = c
            else:
                ans -= mp[c]
                nxt = c
        return ans
```

Jeff首刷
```python
class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):

        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = 0
        sum = 0
        tmp = 0
        while i < len(A):            

            if tmp < 0:
                sum += tmp + dic[A[i]]
                tmp = 0
            elif i + 1 < len(A):
                if dic[A[i+1]] > dic[A[i]]:
                    tmp = -dic[A[i]]
                else:
                    sum += dic[A[i]]
            else:
                sum += dic[A[i]]

            i += 1

        return sum

s = Solution()
print s.romanToInt("X")
print s.romanToInt("V")
print s.romanToInt("XI")
print s.romanToInt("CI")
print s.romanToInt("MMMCCCXXXIII")
```