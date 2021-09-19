# 236. Lowest Common Ancestor of a Binary Tree
Q: Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

![img](imgs/236_1.png)

 

Example 1:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```
Example 2:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

Note:

* All of the nodes' values will be unique.
* p and q are different and both values will exist in the binary tree.


## Ans
高手解較易讀版

這寫法最好記一下。可以跟 235 比較一下，會發現同樣都有一個性質，若 p 跟 q 分別在 root 的兩側，那 LCA 就會是 root，這是最重要的性質，先寫出這性質的code，其他部分的code就容易推敲出來。
```python
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None
        # There is one exception, if p == root or q == root, q or p may be NOT inside the tree from the root.
        # We will handle the situation later.
        if p == root or q == root:
            return root
        # root.left is the entry of left subtree of root. The returned value is the LCA of the left subtree.
        # Note, here we assume a special case. If only one of p and q is inside in the subtree, the return value (LCA) might be p or q, rather than None.
        left = self.lowestCommonAncestor(root.left, p , q)
        # contrast to the above
        right = self.lowestCommonAncestor(root.right, p , q)
        
        # p and q are located at each side of the subtrees. That means the root is the LCA of the tree.
        if left and right:
            return root
        # If left subtree has no LCA, the LCA must be at the right subtree or the root. But since all root cases are considered above, so the LCA must be inside the right subtree, that is the "right" variable.
        if not left:
            return right
        # contrast to the above
        if not right:
            return left
```

高手解精簡版
```python
def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    left, right = (self.lowestCommonAncestor(kid, p, q)
                   for kid in (root.left, root.right))
    return root if left and right else left or right
```


Jeff's 一刷(約花45分不含看過題目):

概念跟高手解不同，但執行速度跟高手解一樣都有到98%，但因code較長，實戰可能不實用，看高手解就好
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node, level):
            if not node or isDone[0]:
                return
            
            if not papa[0]:
                if node in (p,q):
                    papa[0], h[0] = node, level
            else:
                if node in (p,q):
                    isDone[0] = True
                    return

            dfs(node.left, level+1)
            
            if h[0] > level and not isDone[0]:
                papa[0], h[0] = node, level

            dfs(node.right, level+1)

            
        papa, h = [None], [0]
        isDone = [False]
        dfs(root, 1)
        return papa[0]
```

```java
// Runtime: 4 ms, faster than 100.00% of Java online submissions for Lowest Common Ancestor of a Binary Tree.
// Memory Usage: 41 MB, less than 68.33% of Java online submissions for Lowest Common Ancestor of a Binary Tree.
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null)
            return null;
            
        if(p==root || q==root)
            return root;
            
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        
        if(left != null && right != null)
            return root;
        else if(left == null)
            return right;
        else // right == null
            return left;        
    }
}
```