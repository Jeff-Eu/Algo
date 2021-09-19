# 572. Subtree of Another Tree
Q: Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
```
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
```
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
```
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
 ```
Return false.

## Answer

花了約45分才寫正確，比詳解的還好，想法是想將樹用字串表示，再去比較t字串是否為 s字串的子字串，以下是答對前採到的陷阱：
* 一開始選擇用 inorder 的方式，結果被特殊 test input 檢查出是錯的！早知道函式就不要命名成 inorder XD，就命名成 dfs 就好，
* 字串比較錯誤：
    * 不能單純在 dfs 內將字串用 += 的方式最後輸出，否則像 2# 也會是 12# 的子字串，所以必須用 list 去存，最後再轉成字串去比較
    * 還有一種例外，就算最後將 list 轉成字串，下面第二行也會被判斷成第一行的子字串
        ```
        12 # #
        2 # #
        ```
        要避免這種情形就是字串前面要先加個分隔字元(這裡是空白)，原理是讓第一個讀進去的 node 前面也要有個分隔字元，像 _node.val_ 就代表一個真正獨立的node值，才不會混淆進不同的 node 值

```python
# Runtime: 60 ms, faster than 96.51% of Python online submissions for Subtree of Another Tree.
# Memory Usage: 14.7 MB, less than 39.03% of Python online submissions for Subtree of Another Tree.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def preorder(node, ls):
            if not node:
                ls.append("#")
                return
                
            ls.append(str(node.val))
            preorder(node.left, ls)
            preorder(node.right, ls)

        ls1 = [""]
        ls2 = [""]
        preorder(s, ls1)
        s1 = " ".join(ls1)
        preorder(t, ls2)
        s2 = " ".join(ls2)
        return s2 in s1
```

* 新觀念: 如何傳進字串做修改？並output出來？
    * 答: [Python does not make copies of objects (this includes strings) passed to functions](https://stackoverflow.com/questions/13608919/python-how-do-i-pass-a-string-by-reference)
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