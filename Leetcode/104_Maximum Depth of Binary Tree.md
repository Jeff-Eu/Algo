# 104. Maximum Depth of Binary Tree
Q: Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
```
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
```
return its depth = 3.

## Answer
```python
# Runtime: 32 ms, faster than 65.73% of Python online submissions for Maximum Depth of Binary Tree.

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0
            return 1 + max(dfs(node.left), dfs(node.right))
                
        return dfs(root)
```