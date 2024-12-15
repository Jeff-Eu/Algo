## Python General
* 下面是使用 key 的例子，從中可注意到，只要記得先寫 key=... 就對了，降就不容易寫錯
    ```python
    # https://www.programiz.com/python-programming/methods/list/sort
    # Signature from Official Doc: sort(*, key=None, reverse=False)
    arr.sort(key=lambda x : -x)

    # https://www.programiz.com/python-programming/methods/built-in/max
    # Signature from Official Doc: max(arg1, arg2, *args[, key])
    mx = max(str1, str2, str3, key=len)
    ```
* Java vs Python (Comparison)
    * https://compare-versus.blogspot.com/2016/05/comparison-java-vs-python.html
    * 若上面連結失效我有備份在google doc
        * https://docs.google.com/document/d/1dQQecuCyU_27xY0h_rUrS2-vXqtndAdUjclp-hrXwF8/edit#heading=h.v5lzushpbnz0
        
* 寫成 `M = m = 4`，若前面沒宣告過 m，降寫也會宣告 m的變數
* python 沒有 ++ -- 這類的 operator
* [匯入寫法](https://stackoverflow.com/questions/8783261/python-math-module), ex
    - `from math import log`
    - `import math`
* Python如何針對object的排序寫operator => [使用 \_\_lt\_\_ 及 \_\_eq\_\_](https://stackoverflow.com/questions/48313301/python-sort-has-higher-priority-for-lt-than-gt/48313338#48313338)
* [Operator Precedence](https://www.tutorialspoint.com/python/operators_precedence_example.htm)
    * 常見錯誤
        ```python
        out += (n & 1) << move # 注意 << 比 & 的優先權大！
        ```

## Tuple
* 另外注意python語法的陷阱，[tuple直接相加跟預期的不一樣](https://stackoverflow.com/questions/497885/python-element-wise-tuple-operations-like-sum)。正確寫法如下：
    ```python
    import operator
    a=(1,2)
    b=(3,4)
    print tuple(map(operator.add, a, b)) # (4, 6)
    ```

## Math
* [What is the difference between '/' and '//' when used for division?](https://stackoverflow.com/questions/183853/what-is-the-difference-between-and-when-used-for-division)

* 
    ```python
    import math
    print math.sqrt(4) # 2.0
    print math.ceil(4.2) # 5.0
    print math.floor(4.2) # 4.0
    print int(4.2) # 4
    ```
* Random example
    ```python
    import string
    import random
	alphabet = string.ascii_letters + '0123456789'
	code = ''.join(random.choice(alphabet) for _ in range(6))
	print code
    ```
* Random example2：
    ```python
    import random

    random.randint(3, 9)  # 3~9隨機取一值

    choice(ls) # 從ls隨機取一個元素 (ls是一個List)
    ```
* Logarithm function returns a float number, not integer. As [python math function doc said](https://docs.python.org/2/library/math.html), *"The following functions are provided by this module. Except when explicitly noted otherwise, all return values are **floats**."*. 
* In default, divide, "/", and module, "%", both return integer.
* 在Python中，整數相除的結果仍是整數；若是浮點數除以整數會得到浮點數
* int 最大最小值是
    ```
    import sys
    max = sys.maxsize
    min = -sys.maxsize -1
    ```
    (僅在 Python 2； [Python 3移除了int最大值的限制](https://stackoverflow.com/questions/9860588/maximum-value-for-long-integer/9860611#:~:text=maxint%20The%20largest%20positive%20integer,of%202's%20complement%20binary%20arithmetic.))
* float最大值 float("inf") ；最小值 float("-inf")
* Python 3 是使用 math.inf 與 -math.inf (int, float都適用)
    * ref: https://stackoverflow.com/questions/13795758/what-is-sys-maxint-in-python-3
* Python若要算出x的y次方，除了可以import math來使用math.pow(x,y)之外，也可以用x**y的快速寫法

## Misc
* 協助 debug的方法: 使用 print (數字) 放在 if 或 while 裡面。
* 在class裡面呼叫自己其他的method也需要使用 self 嗎？
    https://stackoverflow.com/questions/18679803/python-calling-method-without-self
    - 簡單解釋: 要！ 如果懶的話，就在裡面呼叫 global function
* 學一個新語言要先了解它有無call by ref (pass by ref), [關於Python的](https://stackoverflow.com/a/986145/1613961)
    * Python 跟 js 還有 C, JAVA 一樣，沒有像 C++, C# 有call by ref；像Python這類的是將物件的reference做 call by value的動作，參考,
        * https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
    * How do I pass a string by reference?
        * Ans: No. [Python does not make copies of objects (this includes strings) passed to functions](https://stackoverflow.com/questions/13608919/python-how-do-i-pass-a-string-by-reference)
            * But operations on strings always return a new string object. E.g.
                ```python
                def go(s):
                    print id(s) # 53160848
                    s += "a"
                    print id(s) # 53418752

                s1 = "b"
                print id(s1) # 53160848
                go(s1)
                ```
            * 一般要修改傳進字串的方法，就是將字串存進一個陣列中，例如 
                ```python
                s = ["a"] 
                s[0] += "b"
                print s[0] # ab
                ```
* 標準輸入
    * 讀一行
        ```python
        import sys
        s = sys.stdin.readline()
        ```
    * 把剩下輸入全讀進來
        ```python
        s = ""
        for line in sys.stdin:
            s += line
        arr = s.split()
        ```
* code的簡化命名方式：
    * max => mx
        * max n => mxN
        * local max/min => lmx, lmi
        * absolute max/min => amx, ami
    * sum => sm
    * list => ls
    * heap => hp
    * sorted(arr) => sorArr
    * set => hsh (不要用 _set，因為在hackrank會被視為keyword的顏色)
    * left => l
    * right => r
    * start index => st
    * end index => ed
    * dict/map => mp (Python 有一個 map()函式，跟dictionary無關，所以不要用 map 當 keyword 否則衝到)
    * height/width => h, w
    * adjacent list => adj
    * 1-D array used for dynamic programming => dp[i]