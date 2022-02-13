# 113. Path Sum II
Q: Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,
```
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
```
Return:
```
[
   [5,4,11,2],
   [5,8,4,5]
]
```

## Answer
Jeff's 1刷 (17:41)
```python
# Runtime: 40 ms, faster than 44.74% of Python online submissions for Path Sum II.
# Memory Usage: 19.7 MB, less than 7.14% of Python online submissions for Path Sum II.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        def dfs(node, s, seg):
            if not node:
                return
            
            if not node.left and not node.right and s == node.val:
                seg.append(node.val)
                out.append(seg)
                return

            seg.append(node.val)
            s -= node.val
            
            dfs(node.left, s, seg[:])
            dfs(node.right, s, seg[:])
            
        out = []
        dfs(root, sum, [])
        return out
```
Jeff's 1刷 改良版 (Faster, a little harder)

```python
# Runtime: 36 ms, faster than 67.30% of Python online submissions for Path Sum II.
# Memory Usage: 19.7 MB, less than 7.14% of Python online submissions for Path Sum II.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        def dfs(node, s, seg):
            if not node:
                return
            
            seg2 = seg[:]
            if not node.left and not node.right and s == node.val:
                seg2.append(node.val)
                out.append(seg2)
                return

            seg2.append(node.val)
            s -= node.val
            
            dfs(node.left, s, seg2)
            dfs(node.right, s, seg2)
            
        out = []
        dfs(root, sum, [])
        return out        
```