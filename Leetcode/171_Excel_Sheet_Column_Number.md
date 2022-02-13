# 171. Excel Sheet Column Number
(也是 InterviewBit 的 math problem)\
Q: Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
```
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
```

## 思路
Jeff:\
 這題容易讓人搞混的原因是，它的進位法則不能直接轉換成我們所熟知的N進位法則，我們可以做個小轉換，才能變成熟知的N進位。

若把Z定義成 A0，A0的累計值就等同進一位再加原位變0，即 A0 = 26^1 + 0，而A0加1才會到AA，那這時候的進位規則就會變成跟我們所理解的N進位數一樣，N就會是N=26，所以
```
A = 1
B = 2
Z = A0 = 26^1 + 0 = 26
AA = 26^1 + 1
B0 = 26^2*2 + 0 = B0 = AZ
BA = 26^2*2 + 1

ZA = A0A = 26^2 + 0 + 1
ZB = A0B = 26^2 + 0 + 2
ZZ = Z0 + Z = A00 + A0 = AA0 = 26^2 + 26^1 + 0
ZZZ = Z00 + Z0 + Z = A000 + A00 + A0 = AAA0 = 26^3 + 26^2 + 26^1 + 0
```
### 深入分析：為何不能一開始就換成N進位？

原因是一般的N進位法則中，某一位到了N就會進位，並且原位變成0；但這裡是某一位到了N，並不會進位，而是該位要再加1才會進位，但該位也會變成1(以這題例子就是A)，以下面例子說明本題

從A開始數
```
位數  26^2  26^1  1
數值              1
字母              A
累計值 = 1
```
再到B
```
位數  26^2  26^1  1
數值              2
字母              B
累計值 = 2
```
再到Z
```
位數  26^2  26^1  1
數值              26
字母              Z
累計值 = 26
```
從Z再加1進位到AA
```
位數  26^2  26^1  1
數值         1    1
字母         A    A
累計值 = 26 + 1 = 27
```
接下來繼續累加到AZ
```
位數  26^2  26^1  1
數值         1    26
字母         A    Z
累計值 = 26 + 26 = 52
```
從AZ再加1
```
位數  26^2  26^1  1
數值         2    1
字母         B    A
累計值 = 26*2 + 1 = 53
```
## Jeff 個人筆記
- 若要將字元轉換成unicode數值，可用ord('A')這函式
- 字串S取得某字元可用index寫法，S[0]即取得第一字元
## Answer

Leetcode有[高手解](https://leetcode.com/problems/excel-sheet-column-number/discuss/)，JAVA只用三行就解決。

Jeff's answer
```python
class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        size = len(A)

        i = 0
        nth = size - 1
        result = 0
        while nth >= 0:

            result += (26**nth)*(ord(A[i])-ord('A') + 1)

            i += 1
            nth -= 1

        return result
```