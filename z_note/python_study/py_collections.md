## Python Collections
### Array
* python的陣列跟 List/Stack 是共用同一種
* 初始化二維陣列的寫法，背!!
    ```python
    arr = [[0]*width for _ in xrange(height)]
    ```
    * 錯誤的初始化寫法
        ```python
        # jagged1
        print "jagged1:"
        jagged1 = [[0]*3] * 3  # 或寫成 [0,0,0] * 3
        print jagged1
        jagged1[0][1] = 2

        print jagged1

        '''output
        jagged1:
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        [[0, 2, 0], [0, 2, 0], [0, 2, 0]]
        '''
        ```
        * 記住，只有一維陣列可以用 `[]*N` 的語法初始化，裡面的 item只能是 primitive type !! 否則只是同一塊heap memory複製位址，二維以後陣列初始化就用 comprehension list。

### Jagged Array
初始化的寫法小心寫錯，下面三個例子都是錯的
```python
# jagged1 Wrong !
print "jagged1:"
jagged1 = [[]] * 5
print jagged1
jagged1[0].append(1)
print jagged1

''' output for jagged1:
[[], [], [], [], []]
[[1], [1], [1], [1], [1]]
'''

# jagged2 Wrong !
print "jagged2:"
jagged2 = []*5
for _ in jagged2:
    jagged2.append([])
print jagged2
jagged2[0].append(1)
print jagged2

''' output for jagged2
runtime exception
'''

# jagged3 Wrong !
print "jagged3:"
jagged3 = []*5
print jagged3

for i in jagged3:
    jagged3[i] = [] #list()
print jagged3
jagged3[0].append(1)
print jagged3

''' output for jagged3
runtime exception
'''
```

正確的initialize 應該如下
```python
# jagged 4:
print "jagged4:"
jagged4 = []
for _ in xrange(5):
    jagged4.append([])

print jagged4
jagged4[0].append(1)
print jagged4

'''output jagged 4
[[], [], [], [], []]
[[1], [], [], [], []]
'''

# jagged 5:
print "jagged5"
jagged5 = [[] for r in xrange(5)]

print jagged5
jagged5[0].append(1)
print jagged5

'''output jagged 5
[[], [], [], [], []]
[[1], [], [], [], []]
'''
```
* **心得**：以前初始化二維陣列是會寫成 `[0]*N` ，但初始化 jagged array不能寫成 `[[]]*N`，這種寫法不會自動append新的`[]`進外層的array(就算寫成`[list()]*N`也一樣)；相反的它只是"複製"同一個`[]`進外層的array，換句話說，只有 comprehension syntax 可以為每個item初始化不同的值並append上去，但在`[xxx]*N`的語法中無法針對item做不同的初始化，也就是說`[[]]*N`只能new一次heap memory；只有 comprehension syntax可能各別new heap memory。
    * 只要記住，只有一維陣列可以用 `[]*N` 的語法初始化，裡面的 item只能是 primitive type !! 否則只是同一塊heap memory複製位址，二維以後陣列初始化就用 comprehension list。

### List / Stack
* Python slice的寫法，例如 a[::-1], a[-1:]
    * 重點是 :: 的寫法其實只是將兩個 : 並在一起，中間沒填數值的情況，所以 :: 並不是一個新的符號
    * [Understanding Python's slice notation](https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation)
        * 對於list a 的slice寫法為 `a[start: end: stride]`，從下例可觀察出，若end有寫，則最多終止至index在 end-stride 的位置；若end不寫，則終止至list的兩端，看那一端先到。
            ```python
            a[-1]    # last item in the array
            a[-2:]   # last two items in the array
            a[:-2]   # everything except the last two items

            a[::-1]    # all items in the array, reversed
            a[1::-1]   # the first two items, reversed
            a[:-3:-1]  # the last two items, reversed
            a[-3::-1]  # everything except the last two items, reversed
            ```

    * [Python: What does for x in A[1:] mean?](https://stackoverflow.com/a/44341431/1613961)
    * Slicing 超過範圍不會出錯，e.g.
        ```python
        s = "hello"
        print s[7:100] == ""
        lista = [1, 3, 4]
        print lista[5: 9] == []
        
        # 不會跳exception。會印出
        # True
        # True
        ```
        [引述](https://stackoverflow.com/questions/9490058/why-does-substring-slicing-with-index-out-of-range-work)：[999:9999] isn't an index, it's a slice, and has different semantics. From the python intro: "Degenerate slice indices are handled gracefully: an index that is too large is replaced by the string size, an upper bound smaller than the lower bound returns an empty string."
* list的copy的幾種寫法
    * 用slicing寫，例如`A[:]`會是一份複製`A`的list，例如 `B = A[:]`
    * `B = [] + A`
* A,B兩變數存同一個 list，則 A,B的位址相同：
    ```python
    A = [1,2,3]
    B = A
    C = [] + A
    print id(A) # 59225992
    print id(B) # 59225992
    print id(C) # 59243376
    ```
* [The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found, but find() returns -1.](https://www.w3schools.com/python/ref_string_index.asp)
* List可當stack用，不需額外import library，主要函式是 append()跟pop()。但不能當queue用
* 修改原來List用extend()，要注意裡面記得加括號 e.g.
    ```python
    arr = [1, 2]
    arr.extend([3, 4]) # Correct, arr is [1, 2, 3, 4]
    # arr.extend(3, 4) # Wrong
    ```
    兩 list相加會回傳新的 list
    ```python
    arr = [1, 2]
    arr2 = arr + [3, 4]
    print arr2 # [1, 2, 3, 4]
    ```
* [Traverse a list in reverse order in Python](https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python)
    ```python
    >>> a = ["foo", "bar", "baz"]
    >>> for i in reversed(a):
    ...     print(i)
    ... 
    baz
    bar
    foo
    # No copy is created, the elements are reversed on the fly while traversing! This is an important feature of all these iteration functions (which all end on “ed”).
    # e.g. sort vs sorted, reverse vs reversed (有加ed的是回傳新創建的，沒加ed的是修改原本的)
    ```
* [list reverse 的三種方式](https://dbader.org/blog/python-reverse-list)
- 關於 list 插入到最後的寫法
    - 插入原來的list
        list.append(1)
    - 回傳新的list
        list_new = list + [1]
* [Sort list of pairs](https://stackoverflow.com/questions/8459231/sort-tuples-based-on-second-parameter)
    ```python
    my_list.sort(key=lambda x: x[1])
    ```
* key=len 例如 sort(s, key=len)   或像是   max(s1, s2, s3, s4, key=len)

* [How do I check if a list is empty?](https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty)
    ```python
    if not a:
        print("List is empty")
    ```
* [Is there a short contains function for lists?](https://stackoverflow.com/questions/12934190/is-there-a-short-contains-function-for-lists)
    ```python
    if myItem in list:
        # do something
    
    # Also, inverse operator:

    if myItem not in list:
        # do something
    ```
* List equality
    ```python
    >>> [0,1,2] == [0,1,2]
    True
    >>> [0,1,2] == [0,2,1]
    False
    >>> [0,1] == [0,1,2]
    False
    >>> id([1,2]) == id([1,2])
    True
    >>> id(A) == id(B)  # if A=[1,2] B=[1,2]
    False # 這結果跟上一個例子不同，python的compiler處理滿特別
    ```
* 若`words`是一個List，則`dict_count = collections.Counter(words)`可用來計數相同的值各有幾個，將它們存在一個字典, `dict_count`
    * 注意這時候在列舉 dict_count 時，並不會按照count數來排序，但若直接 print dict_count，卻是按照count數來排序，若要按count數descending排序(由大至小)，可用 dict_count.most_common() 這方法，它會回傳一個陣列，並不像 dict_count.items() 只回傳列舉，所以用 most_common() 會很耗效能。

* list sort 的comparer寫法
    ```python 2
    ...
    def compare(l1, l2):
        if l1[0] < l2[0]:
            return -1
        elif l1[0] > l2[0]:
            return 1
        else:
            return 0

    ln = sorted(intervals, cmp=compare)
    ```
    cmp在Python3已經拿掉，Python3的寫法：
    ```python 3
    from functools import cmp_to_key

    ln = sorted(intervals, key=cmp_to_key(compare))

    def compare(self, l1, l2):
        if l1[0] < l2[0]:
            return -1
        elif l1[0] > l2[0]:
            return 1
        else:
            return 0
    ```
   除非判斷式複雜，否則直接用key的lambda寫比較快
   ```python
   ln = sorted(intervals, key=lambda x: x[0])
   ```
* 比較兩個 list 是否為同一物件參照要用`is`；比較他們的內容是否一樣要用`==`
    ref: [Comparing lists by reference vs value in Python](https://stackoverflow.com/questions/14080970/comparing-lists-by-reference-vs-value-in-python)


* 有一個list為`[3,7,8,2]`，它的和快速求出：`sum([3,7,8,2])`
### Queue
* [using queue by list] 注意雖然使用 list 也可以達到 queue的效果，但效能很差，不推薦使用
    Ref: https://www.geeksforgeeks.org/queue-in-python/

```python
# simulate a queue by list
queue = []
  
# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')
  
print("Initial queue")
print(queue)
  
# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
  
print("\nQueue after removing elements")
print(queue)

'''output:
Initial queue
['a', 'b', 'c']

Elements dequeued from queue
a
b
c

Queue after removing elements
[]
'''
```

* [Official guide for Queue object](https://docs.python.org/2/library/queue.html#queue-objects)
    ```python
    from Queue import Queue # Python 2
    # import queue          # Python 3

    q = Queue()         # Python 2
    # q = queue.Queue() # Python 3

    q.put(2)
    if not q.empty():
        p = q.get() # pop the q (Yes, it's get(). No doubt !!)

    # 2 is printed
    print p
    ```
* 亦可使用[deque (double ended queue)](https://pymotw.com/2/collections/deque.html)，這樣就不用額外再去記上面Queue的用法(但是最方便的還是用list模擬)，另外deque有一些原本List(以及所隱含的stack)的操作支援，所以同樣支援index(), remove(), append(), pop(), extend()，但它新增了 popleft(), appendleft(), extendleft()，注意 extendleft()是一個個添加到左邊。
    * deque 若要當作是純 queue ，那你可以選擇要往左或往右 pop：
        * 往左 pop 的queue: popleft, append
        * 往右 pop 的queue: pop, appendleft 

### Set
* 新增為 add(), 移除可用 remove()或 discard()，都不會回傳，這兩個差別在，如果要移除的元素不在set裡面，discard不會跳 exception，
    ```python
    hashset = set()
    hashset.add(3) # 3
    hashset.add(8) # 3, 8
    hashset.remove(3) # 8
    hashset.discard(7) # 8 (nothing changed)
    ```
* 若新增重覆的值進 set，它並不會raise error，必須要自行用 if-else判斷。
* 要從set中移除並取出任意一值： `item = myset.pop()` ，如果不想移除該值只想peek的寫法是 `next(iter(mp[val]))`
    * from https://stackoverflow.com/questions/59825/how-to-retrieve-an-element-from-a-set-without-removing-it
* [DefaultDict](https://www.geeksforgeeks.org/defaultdict-in-python/):
    * Defaultdict is a sub-class of the dict class that returns a dictionary object. The functionality of both dictionaries and defualtdict are almost same except for the fact that defualtdict never raises a KeyError. It provides a default value for the key that does not exists.
        ```python
        from collections import defaultdict
        # Function to return a default 
        # values for keys that is not 
        # present 
        def def_value(): 
            return "Not Present"
            
        # Defining the dict 
        d = defaultdict(def_value) 
        d["a"] = 1
        d["b"] = 2

        print(d["a"]) 
        print(d["b"]) 
        print(d["c"])

        # Output:
        # 1
        # 2
        # Not Present
        ```
    * Next example:
        ```python
        from collections import defaultdict
        # 預設為 0 的 dictionary
        mp = defaultdict(int)
        mp["a"] += 3
        print mp["a"] # 印出3
        ```

### Dictionary 
* 初始化: `dic = dict()` 或是 `dic = {}`
    * 有值的初始化例如： `mp = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}`
* [python delete](https://thispointer.com/different-ways-to-remove-a-key-from-dictionary-in-python/)有 del 跟 pop()兩種，後者是可以將value取出，pop()又有分有default值的，有default值的不會跳exception (del會跳exception)。
    ```python
    removed_value = dic.pop('f')
    removed_value = dic.pop('f', 'default')
    ```
* 列舉方法
    ```python
    for key in mydict:
        ...
    for key, value in mydict.items():
        ...
    for key in mydict.keys():
        ...
    for value in mydict.values():
        ...
    ```
* 取出的兩種方式
    ```python
    dic.get(3, 0) # 如果取不到會以 default值為 0 代替
    dic[3] # 若取不到會跳例外
    ```
### Collections comprehension / Generator
* [List/Set/Dictionary Comprehension](https://zh.wikipedia.org/wiki/List_comprehension) (常會將for簡化成一行的寫法)
    * [List comprehension基本介紹](https://yuchungchuang.wordpress.com/2017/08/16/python-%E4%B8%B2%E5%88%97%E7%B6%9C%E5%90%88%E8%A1%A8%E9%81%94%E5%BC%8F-list-comprehension/)
    * [各種comprehension完整解晰，包含很重要的generator](https://realpython.com/list-comprehension-python/)
    * ex1
        ```python
        >>> x = [i for i in range(10)]
        >>> x
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        ```
    * ex2
        ```python
        (a, b) = (1, 3)
        print a, b
        a, b = (5, 7)
        print a, b
        a, b = (i for i in (3, 4))
        print a, b
        # a, b = i for i in (3, 4)  # invalid syntax (missing parentheses)
        '''
        output:
        1 3
        5 7
        3 4
        '''
        ```