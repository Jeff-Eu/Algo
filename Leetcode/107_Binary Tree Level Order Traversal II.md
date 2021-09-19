# 107. Binary Tree Level Order Traversal II
Q: Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
```
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
```
return its bottom-up level order traversal as:
```
[
  [15,7],
  [9,20],
  [3]
]
```
## Answer

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        level = [root]
        out = []        
        while level:
            out.append([node.val for node in level])
            level = [n for node in level for n in (node.left, node.right) if n]
            
            
        return out[::-1]
```

以下是改進網友的 Kotlin寫法，注意：
* 雖然是要回傳 List<List<Int>> 但結果回傳 List<ArrayList<Int>> 竟然也可以過！
* ArrayQueue 的 offer() 跟 add() 是一樣的
    * offer() = add() = addLast() = offerLast <-> addFirst() = offerFirst()
* 以前在 python 對 Level Order 的寫法只會有 list comprehension，降就沒有用到 queue了，並且在重新創建 list 物件時會耗效能；下面的做法讓 Level Order 也可以用 queue去實現，關鍵在於可先取得 queue.size ，子迴圈只要跑 queue.size 次去 pop queue，之後同時 add 進下一層的子元素進 queue 時也不用擔心會 pop 到子元素了(參考下面code)。

```java kotlin
/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
// Runtime: 180 ms, faster than 93.33% of Kotlin online submissions for Binary Tree Level Order Traversal II.
// Memory Usage: 35.9 MB, less than 55.56% of Kotlin online submissions for Binary Tree Level Order Traversal II.
    fun levelOrderBottom(root: TreeNode?): List<List<Int>> {
        if (root == null) return listOf()

        val res = ArrayList<List<Int>>()
        val q = ArrayDeque<TreeNode>()

        q.add(root)

        while (!q.isEmpty()) {
            val list = ArrayList<Int>()

            for (dummy in 1..q.size) {
                val node = q.poll()

                list.add(node.`val`)

                if (node.left != null) q.add(node.left)
                if (node.right != null) q.add(node.right)
            }
            res.add(list)
        }

        return res.reversed()
    }
}
```
