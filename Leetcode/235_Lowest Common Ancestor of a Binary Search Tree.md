# 235. Lowest Common Ancestor of a Binary Search Tree
Q: Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

![](imgs/235_1.png)


```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```
Example 2:

![](imgs/235_1.png)
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```
Example 3:
```
Input: root = [2,1], p = 2, q = 1
Output: 2
```
## Answer

發現到它是 BST 之後才花了約40分解出
* 新技能: 要對兩個 boolean 變數分別叫 a 及 b 做 xor 運算，只要做 a != b 即可
```python
# Runtime: 64 ms, faster than 89.29% of Python online submissions for Lowest Common Ancestor of a Binary Search Tree.
# Memory Usage: 21.3 MB, less than 83.75% of Python online submissions for Lowest Common Ancestor of a Binary Search Tree.
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while True:
            if root.val == p.val or root.val == q.val: # note, remember to handle the equal situation
                return root
            
            if (root.val < p.val) == (root.val > q.val): # note, `==` operator has higher priority than `<>` operators
                return root
            else:
                if root.val < p.val: # don't worry to handle the null value here because we will find LCA first :)
                    root = root.right
                else:
                    root = root.left
                    
        return None
```

下面是kotlin的code (null check寫起來真是有些麻煩)
* 關於kotlin的語法
    * 因為val是keyword，所以成員field若要取相同名稱要加`的引號(注意不是')
        * e.g.  root.`val`
    * 無論變數是否為nullable都可以使用 ? 去取值，例如 root!!?.`val`
    * method的參數皆為 val
    * ternary的寫法跟python在if的地方剛好顛倒過來，kotlin的寫法嚴格來講算是把多行的if-else寫法縮減成一行而已，所以kotlin不算有真正的ternary operator。

* 演算法實戰中因為nullable 變數的寫法不太方便，還是改用java較好
```java kotlin
/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int = 0) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
        var root2 = root
        while(true) {

            if(root2?.`val` == p?.`val` || root2?.`val` == q?.`val`)
                return root2
            
            if(root2?.`val`!! < p?.`val`!! == root2?.`val`!! > q?.`val`!!)
                return root2
            else
                root2 = if(root2.`val` < p.`val`) root2.right else root2.left
        }
        
        return null
    }
}
```