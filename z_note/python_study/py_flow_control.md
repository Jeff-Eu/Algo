# Python Flow Control
* Python Loop
    * [w3school: Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)
        ```python
        fruits = ["apple", "banana", "cherry"]
        for x in fruits:
            print(x)

        for x in "banana":
            print(x)
        ```
    * Python的for不像一般語言的for一樣能在for的那行做三件事情的statements，所以在一般語言若該行for的statements很複雜，在Python就只能轉成while來寫：\
        例如java的
        ```java
        for(i=0; i<10; i++)
            // do sth...
        ```
        Python需用
        ```python
        i=0
        while i<10:
            # do sth...
            i+=1
        # Or
        for i in xrange(10):
            # do sth...
        ```
    * Python沒有do-while，要模擬do-while可降做
        ```python
        while True:
            do_something()
            if condition():
                break
        ```

* The `enumerate()` method adds counter to an iterable and returns it (the enumerate object)，方便之處在於，若要列舉array全部的項目，需要index跟value時，就不需用 `for i in xrange(len(array))`的寫法，因為這時取value要寫成 `array[i]`，較易出錯。
    * The syntax of enumerate() is:\
        (注意，它的 start 參數不是指從第幾個元素開始尋訪，而是將下標的數字換成從第 i 開始計數；所以全部的元素都還是有被尋訪到。)
        ```python
        enumerate(iterable, start=0)
        ```
    * https://www.geeksforgeeks.org/enumerate-in-python/
    * http://www.runoob.com/python/python-func-enumerate.html

    ```python
    # Python program to illustrate 
    # enumerate function in loops 
    l1 = ["eat","sleep","repeat"] 
    
    # printing the tuples in object directly 
    for ele in enumerate(l1): 
        print ele 
    print 
    # changing index and printing separately 
    for count,ele in enumerate(l1,100): 
        print count,ele 
    ```
    output
    ```
    (0, 'eat')
    (1, 'sleep')
    (2, 'repeat')

    100 eat
    101 sleep
    102 repeat
    ```

- range 相關
    - [基本用法](https://www.runoob.com/python/python-func-range.html)
        ```python
        >>>range(10)        # 从 0 开始到 10
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> range(1, 11)     # 从 1 开始到 11
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        >>> range(0, 30, 5)  # 步长为 5
        [0, 5, 10, 15, 20, 25]
        >>> range(0, 10, 3)  # 步长为 3
        [0, 3, 6, 9]
        >>> range(0, -10, -1) # 负数
        [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
        >>> range(0)
        []
        >>> range(1, 0)
        []
        ```
    - range("hello") 回傳的是一組 iterator
    - range(4) 回傳的是一組 iterator
    - [What is the difference between range and xrange functions in Python 2.X?](https://stackoverflow.com/questions/94935/what-is-the-difference-between-range-and-xrange-functions-in-python-2-x)
        * xrange only keeps one number in memory at a time. range keeps the entire list of numbers in memory.
        * Personally, I always use .range(), unless I were dealing with really huge lists -- as you can see, time-wise, for a list of a million entries, the extra overhead is only 0.04 seconds.
    - 若不想取出range的每一個值，可直接寫成
        ```python
        for _ in range(6):
            # do sth
        ```
* Ternary Operator in Python
    ```python
    # Program to demonstrate conditional operator 
    a, b = 10, 20
    # Copy value of a in min if a < b else copy b 
    min = a if a < b else b     
    print(min) # 10
    ```
    注意下面的寫法
    ```python
    print 10 if 3 < 10  # invalid syntax: not ternary operator 
    if 3 < 10: print 10 # correct: common if condition
    print 10 if 3 < 10 else 3 # correct: ternary operator
    ```
* None 與物件R的or結果為R，and結果為None
    ```python
    print None or "z" # z
    print "y" or "z" # y
    print None or [] # []
    print None and [] # None
    ```
* NoneType is the type for the None object, which is an object that indicates no value.
    * 用來檢查是否為None，如果 val 不為None，則下列四寫法結果基本上會一樣
    ```python
    if val != None:
        print True

    if not (val is None):
        print True

    if val is not None:
        print True

    if val:
        print True

    # 注意用if判斷0也算是False
    if not 0:
        print True
    # 因此若要循訪某陣列A的各別元素a是否為None時，"不可"用下面這種寫法，所以陣列內元素若是nullable，建議要用 xxx == None 來取代 not xxx 的用法，才能避免誤判。
    A = [None, None, 0]
    for a in A:
        if not a: # 必須改為 a == None
            print str(a) + " is None"
    # output:
    # None is None
    # None is None
    # 0 is None 
    ```
    [補充1](https://stackoverflow.com/questions/7816363/if-a-vs-if-a-is-not-none/7825137#7825137)，下面的code會印出`"all empty"`
    ```python
    arr = []
    hashset = set()
    dictionary = {}
    none = None
    if not arr and not hashset and not dictionary and not none:
        print "all empty"
    ```
    補充2，非空非None即為真
    ```python
    if None or "a": print "a" # a
    if "b" or "a": print "b" # b
    ```

* 2D陣列或3D陣列的存取精簡寫法：
遇到2D陣列上某元素的上下左右需要access時，可以用下面這種寫法
```python
for j in xrange(2):
	for k in [1, -1]:
		if j==0:
			p = (m+k, n)
		else:
			p = (m, n+k)
```
同理，在3維空間中需要access上下左右前後，可以用下面這種寫法
```python
for i in xrange(3):
	for j in [1, -1]:
		if i==0:
			p = (a+j, b, c)
		elif i==1:
			p = (a, b+j, c)
		else:
			p = (a, b, c+j)
```

- [else clause on the for statement](http://docs.python.org/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
	- Loop statements may have an `else` clause; it is executed when the loop terminates through exhaustion of the iterable (with [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)) or when the condition becomes false (with [`while`](https://docs.python.org/3/reference/compound_stmts.html#while)), but not when the loop is terminated by a [`break`](https://docs.python.org/3/reference/simple_stmts.html#break) statement.
	- E.g. [[Finding Sublist]]