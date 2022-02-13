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

## 思路
Jeff: 用我之前在#171的"深入分析"裡面帶的觀念，可以快速解開

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