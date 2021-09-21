## Python String
* 字串<->int
    * 字串轉int => `int("28")`
    * int轉字串 => `str(28)`
* 字元<->數字
    * 字元轉數字 `ord("c")`
    * 數字轉字元 `chr(13)`
* 字元 c
    * c.isalpha()  # 是字母嗎
    * c.isalnum()  # 是字母或數字嗎
* 找substring從第幾個index開始用 find() 或 index()，例如 "abcd".find("cd")會得到 2。兩者的差異是 find 找不到時會回傳-1，index則會拋錯
* join的用法(String的方法)
    ```python
	# 注意每個元素必須要是字串才可以被 join
    myTuple = ("John", "Peter", "Vicky")
    x = "->".join(myTuple)
    print(x) # John->Peter->Vicky
    ```
* [當字串需要更新某個字元時，沒辦法做像s[i]='c'這樣的更新，請先轉成List](https://stackoverflow.com/questions/1228299/changing-one-character-in-a-string-in-python)
    ```python
    >>> s = list("Hello zorld")
    >>> s
    ['H', 'e', 'l', 'l', 'o', ' ', 'z', 'o', 'r', 'l', 'd']
    >>> s[6] = 'W'
    >>> s
    ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
    >>> "".join(s)
    'Hello World'
    ```
