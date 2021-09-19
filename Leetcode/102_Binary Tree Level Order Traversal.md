# 102. Binary Tree Level Order Traversal
Q: Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
```
    3
   / \
  9  20
    /  \
   15   7
```
return its level order traversal as:
```
[
  [3],
  [9,20],
  [15,7]
]
```

## Answer
[高手解](https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33464/5-6-lines-fast-python-solution-(48-ms)):

`level` is a list of the nodes in the current level. Keep appending a list of the values of these nodes to `ans` and then updating `level` with all the nodes in the next level (kids) until it reaches an empty level. Python's list comprehension makes it easier to deal with many conditions in a concise manner.

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        out = []
        level = [root]
        
        while level:
            out.append([n.val for n in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]        
        return out
```
Jeff's 二刷
```python
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        tmp = [root]
        out = []
        while tmp:
            out.append([n.val for n in tmp])
            tmp = [kid for n in tmp for kid in (n.left, n.right) if kid]
        return out       
```

Jeff's 一刷 (使用Queue)
```python
# Runtime: 16 ms, faster than 96.75% of Python online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 13.4 MB, less than 5.88% of Python online submissions for Binary Tree Level Order Traversal.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        q = collections.deque([(root, 1)])
        out = []
        part = []
        current = 0
        while q:
            token = q.popleft()
            if not token[0]:
                continue
            
            if token[1] > current:
                part = [token[0].val]
                current += 1
                out.append(part)
            else:
                part.append(token[0].val)
                
            q.append((token[0].left, token[1]+1))
            q.append((token[0].right, token[1]+1))
            
        return out
```
