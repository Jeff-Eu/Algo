# 112. Path Sum
Q: Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,
```
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
```
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

## Answer
Jeff's 一刷 (14:26)
```python
# Runtime: 36 ms, faster than 48.97% of Python online submissions for Path Sum.
# Memory Usage: 16.5 MB, less than 6.82% of Python online submissions for Path Sum.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        result = [False]
        def dfs(node, s):
            if result[0]:
                return
            
            if not node:
                return
            
            s += node.val
            
            if not node.left and not node.right:
                if s == sum:
                    result[0] = True
                return
            
            dfs(node.left, s)
            dfs(node.right, s)
            
        dfs(root, 0)
            
        return result[0]
```
高手解:
```python
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    # 1:27
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val

return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
```