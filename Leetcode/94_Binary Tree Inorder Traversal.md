# 94. Binary Tree Inorder Traversal
Q: Given a binary tree, return the inorder traversal of its nodes' values.

Example:
```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```
Follow up: Recursive solution is trivial, could you do it iteratively?

## Answer

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # iteratively
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """ 
        stack = []
        r = []
        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return r

            v = stack.pop()
            r.append(v.val)
            root = v.right
            
        return r

#------------------------------

    # recursively
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """ 
        arr = []
        def dfs(r):
            if not r:
                return
            
            dfs(r.left)
            arr.append(r.val)
            dfs(r.right)
            
        dfs(root)
        return arr
```