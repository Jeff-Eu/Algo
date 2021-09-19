# 671. Second Minimum Node In a Binary Tree
Q: Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
```
Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
```

Example 2:
```
Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
```
## Answer

Jeff's (DFS)
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        
        def search(node):
            if node == None:
                return
            elif node.val > root.val:
                if node.val < s[0] or s[0] == -1:
                    s[0] = node.val
                
            search(node.left)
            search(node.right)
            
        s = [-1]
        search(root)
        return s[0]
```

## Approach #1 Depth-first Search [Accepted]


```javascript
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var findSecondMinimumValue = function(root) {
    if (root === null) return -1;
    var min = root.val;
    var sec = Number.POSITIVE_INFINITY;
    var findMin = function(node) {
        if (min < node.val && node.val < sec) {
            sec = node.val
        } else if (node.val === min) {
            if (node.right !== null) findMin(node.right);
            if (node.left !== null) findMin(node.left);
        }
    };
    
    findMin(root);
    
    if (sec === Number.POSITIVE_INFINITY) return -1;
    
    return sec;
};
```