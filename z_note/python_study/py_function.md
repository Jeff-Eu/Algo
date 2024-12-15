## Python Function
* Nested function 如果要使用外層的local變數會遇到一個常見問題，使用技巧=>宣告成陣列
    * Example
        ```python
        def outer():
            def inner():
                ctr[0] += 1
            ctr = [0]
        ```
    * 參見
        * [UnboundLocalError with nested function scopes](https://stackoverflow.com/questions/2609518/unboundlocalerror-with-nested-function-scopes/2609593#2609593)
        * [Python nested functions variable scoping](https://stackoverflow.com/questions/5218895/python-nested-functions-variable-scoping/13277359#13277359)
* Default parameters, ex:
    ```python
    def backtrack(s = "Hello", n = " World"):
        print s + n # Hello World
    ```