# Power of Two Integers
Q: Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

Example
```
Input : 4
Output : True  
as 2^2 = 4. 
```

## Jeff 個人筆記
- Python若要算出x的y次方，除了可以import math來使用math.pow(x,y)之外，也可以用x**y的快速寫法
- Python的for不像一般語言的for一樣能在for的那行做三件事情的statements，所以在一般語言若該行for的statements很複雜，在Python就只能轉成while來寫
- Python沒有do-while，要模擬do-while可降做
    ```python
    while True:
        do_something()
        if condition():
            break
    ```

## Answer

### 思路
x^y 因為指數次方(y)的成長速度較快，因此用兩個while迴圈來尋訪時，外迴圈用x，內迴圈用y，降才有效率

Jeff's code
```Python
class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        a = 1
        p = 2
        
        if A == 1:
            return True
        else:
            while True:
                a += 1
                x = a**p
                if x == A:
                    return True
                elif x > A:
                    break

                while True:
                    p += 1
                    x = a**p
                    if x == A:
                        return True
                    elif x > A:
                        p = 2
                        break

            return False    
```
