# 整理排列組合問題
## 排列組合主要分類
* A. 排列 Permutaion
    * B. 一般排列 ex: [2,1,4,5] 列出全部排法。
        * Math Ans: 4!種
        * Leetcode:
            * [46. Permutations](https://leetcode.com/problems/permutations/)
    * C. 一般選取排列 ex: [2,1,4,5] 選3個，每個數字只可選一次，求全部排法。 
        * Math Ans: P(4,3) 亦即，P4取3，亦即 4*3*2 = 4!/(4-3)! = 24種
    * D. 重覆選取排列 ex: [2,1,4,5] 選3個，每個數字可重覆選取，求全部排法。
        * Math Ans: 4 * 4 * 4 = 64種
    * E. 重覆排列 ex: [3,3,5,5] 列出全部排法。
        * Math Ans: 4!/(2!*2!) = 6
        * Leetcode:
            * [47. Permutations II](https://leetcode.com/problems/permutations-ii/)
* 組合 Combination (Subsets也是一種組合)
    * F. 一般組合 ex: [2,1,4,5,6] 選3個，每個數字只可選一次，求全部組合。
        * Math Ans: C(5,3) 亦即, C5取3 = P(5,3)/3! 5!/(5-3)!/3! = 10
        * Leetcode:
            * [77. Combinations](https://leetcode.com/problems/combinations/)
            * [78. Subsets](https://leetcode.com/problems/subsets/)
    * G. 重覆物件的一般組合 ex: [2,2,2,1,1,3] 選2個，每個元素只可選一次，求全部組合。
        * Math Ans: 高中好像沒提過有它的公式，但做過下面幾個 Leetcode 此類的題目後，猜想先將數列做完排序，就能再從迴圈的規則中導出數學公式。......[Todo: 有空來研究]
        * Leetcode:
            * [90. Subsets II](https://leetcode.com/problems/subsets-ii/)
            * [15. 3Sum](https://leetcode.com/problems/3sum/)
                * 但此題因為只有3個變數的和，所以可以利用[1. Two Sum](https://leetcode.com/problems/two-sum/)的輔助使用比較快的解法。
            * [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
    * H. 重覆組合 ex: [2,1,4,5] 選3個，每個數字可重覆選取，求全部組合。
        * 其實"重覆組合"算是"重覆物件的一般組合"的一種特例
        * Math Ans: [此連結推導如何求出公式：H(4,3)](http://www.math.nsysu.edu.tw/eprob/PerComb/repComb/index.html)
        * Leetcode:
            * [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
                * 此題算是重覆組合問題再加上新的條件，算是再進階一點的變化
            * [322. Coin Change](https://leetcode.com/problems/coin-change/)
                * 算是 39 題的進階版，因存在 DP 解，所以若用單純列舉的方法會超時。

## 歸納觀察
* 組合
    * 可以發現到組合問題只要牽涉到有重覆的，想濾掉這些重覆的組合之前，至少都要先用排序(除非是用 hash set)。
        * 但像 47. Permutations II 就可以不需要先做 sort。
            * 理由: 去看 47. Permutations II 的 code，一樣會有一個 set 用來篩選重覆的數，這個在 90. Subsets II 的寫法是一樣的，但這作法是用來濾除"一模一樣的排列"，卻不能濾除"相同組合卻排列不同"的情況；因為組合的選擇不像排列一樣不考慮順序性，因此第90題屬於的"重覆物件的一般組合"問題要先做sort，才能避免選到不同順序的組合。例如：[4,4,1,4] 選3個，[4,4,1]跟[4,1,4]就算不同順序的組合。

* 比較迭代 dfs 的地方：
    * A類
        * 46. Permutations
            ```python
            def dfs(path, ls):
                
                for i in xrange(len(ls)):
                    v = ls.pop(i)
                    dfs(path + [v], ls) # 將剩下的 list餵進 dfs，還有其他方式，這種算是比較有效率的
                    ls.insert(i, v)
            ```

    * B類
        * 39. Combination Sum
            ```python
            def dfs(idx, path):
                for i in xrange(idx, len(nums)):
                    dfs(i, path + [nums[i]])
            ```

    * C類
        * 77. Combinations
            * 可以將 dfs的寫法改成直接輸出解，觀察看看，參數寫法不一樣之處。
        * 78. Subsets
        * 90. Subsets II
        * 18. 4Sum 
            * 此題為變形題，還要注意兩處
                * dfs的寫法為了改成直接輸出解，觀察看看，其參數寫法不一樣之處(也可應用在 77. Combinations)。
                * 此外，因為該函式解可以遞迴到 1. Two Sum 的快速解，必須要用到該快速解才不會像單純列舉所有組合而超時。。
        * 40. Combination Sum II
        * 216. Combination Sum III (77題的小小進階版)
            ```python
            def dfs(idx, path):
                for i in xrange(idx, len(nums)):
                    dfs(i+1, path + [nums[i]])
            ```
            * 可以發現在迭代 dfs 的地方，B類與C類餵進去 i 的起始位置的不同處，B類是 i 而 C類是 i+1。
            * 承上，那是因為B類沒有限制同一個元素能重覆選取幾次，如果有限制，比如說求 [1,4,7] 裡每個元素最多選3個組合，那就可以將 [1,4,7] 展開成 [1,1,1,4,4,4,7,7,7] ，再對它去求Subsets II 的問題，這時就變成了C類，也從i+1開始。