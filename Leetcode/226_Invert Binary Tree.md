# 226. Invert Binary Tree
Q: Invert a binary tree.

Example:

Input:
```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```
Output:
```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```
Trivia:
This problem was inspired by this original tweet by Max Howell:
```
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
```
## Answer
```python
# Runtime: 12 ms, faster than 96.27% of Python online submissions for Invert Binary Tree.
# Memory Usage: 13.8 MB, less than 7.24% of Python online submissions for Invert Binary Tree.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node, r): # pre-order
            r.val = node.val
            
            if node.left:
                r.right = TreeNode()
                dfs(node.left, r.right)
            
            if node.right:
                r.left = TreeNode()
                dfs(node.right, r.left)

        if not root:
            return None
        root2 = TreeNode()
        dfs(root, root2)
        return root2
```