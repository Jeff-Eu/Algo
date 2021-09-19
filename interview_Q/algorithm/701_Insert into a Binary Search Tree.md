# 701. Insert into a Binary Search Tree
Q: Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:

        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4

## Answer

Jeff's answer - recursive，非破壞式 (效能較好一點)
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.insertTreeNode(root, val)
        return root

    def insertTreeNode(self, node, val):

		if node.val > val:
			if node.left is not None:
				self.insertTreeNode(node.left, val)
			else:
				node.left = TreeNode(val)
		elif node.val < val:
			if node.right is not None:
				self.insertTreeNode(node.right, val)
			else:
				node.right = TreeNode(val)
```

Wiki介紹的解法 - recursive，破壞式
```python
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        elif root.val < val:
            root.right =  self.insertIntoBST(root.right, val)
        
        return root
```