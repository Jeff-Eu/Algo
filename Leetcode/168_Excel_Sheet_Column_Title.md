# 168. Excel Sheet Column Title
Q: Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

這題跟#171是姊妹題, 在 InterviewBit 的 math 分類也有


## Jeff 個人筆記
- 在python中 
    - x = 30 / 7 會等於 4，不會有小數點
    - 在python中，要使用某特定數學函式，可以寫成
    ```python
    from math import log
    ```
    - int(3.14)會等於3，int(...)會將小數點捨去
    - list 的合併可降寫 [3, 2] + [5] 就會等於 [3, 2, 5]
    - range會回傳一個list, range(5, 1, -1)會回傳 [5, 4, 3, 2]

## Answer

Jeff二刷，解釋一下觀念，這裡先觀察到有26種不同的字母，所以是26進位；這是因為以前學的進位系統有幾個數字就是幾進位。

再來，以一般的進位系統來說，比如說，給你一個十進位數，如何轉成8進位，會有兩個現象：
* 都是用除法的商與餘數來求得
* 都是從0開始計算

但在這題中，可以發現 A 是從 1 開始，所以為了mapping到我們所認識的進位系統，先將它減1，讓A從0開始計算，接下來才求餘數，
進而利用餘數找出最右邊的字母；而從右邊第二位開始，我們一樣照原本進位系統的規則，用商再去計算，但商最少也會是1，如果再回去
`chr(r + numberA)`的式子會造成字母至少從B開始算，所以我們才會先將商做減1的動作：`c = c / 26 - 1`，讓第二個字元一樣對應從0開始算。

```python
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        c = columnNumber - 1
        r = 0
        numberA = ord('A')
        ans = ""
        while c > 25:
            r = c % 26
            ans = chr(r + numberA) + ans
            c = c / 26 - 1

        ans = chr(c + numberA) + ans
        return ans
```



這邊用到我之前在#171的"深入分析"裡面帶的觀念
Jeff's new answer
```python
class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        res = ""
        while A > 0:
            A -= 1
            res = chr(A % 26 + ord('A')) + res
            A = A / 26

        return res
```

Jeff's old answer (not good)
```python
from math import log
class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):

        nth = int(log(A, 26))
        res = ""
        myList = []
        while nth >= 0:

            num = int(A / (26**nth))
            myList += [num]
            A -= (26**nth)*num
            nth -= 1

        for i in range(len(myList)-1, -1, -1):
            if myList[i] <= 0:
                if i != 0:
                    myList[i] = 26 + myList[i]
                if i > 0:
                    myList[i-1] -= 1

            if i == 0:
                res = ""
                for j in range(len(myList)):
                    if j == 0 and myList[j] < 1:
                        continue                        
                    res += chr(myList[j] - 1 + ord('A'))

        return res
```