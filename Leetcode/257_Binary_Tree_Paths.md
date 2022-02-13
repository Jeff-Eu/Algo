# 257. Binary Tree Paths
Q: Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:
```
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
```
## Answer

Jeff's
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        stack = []
        result = []
        def inorder(node):
            if not node:
                return
            if not node.left and not node.right:
                stack.append(str(node.val))
                s = "->".join(stack)
                result.append(s)
                stack.pop()
                return
                
            stack.append(str(node.val))
            inorder(node.left)
            inorder(node.right)
            stack.pop()
            
        inorder(root)
            
        return result
```

學平's
* Depth first Traversal

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
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
    var ans = [];
    
    var DFS = function(root, path, ans) {
        if (root.left === null && root.right === null) {
            ans.push(path + root.val);
        }
        if (root.left !== null) DFS(root.left, path + root.val  + '->', ans);
        if (root.right !== null) DFS(root.right, path + root.val + '->', ans);
    };
    
    if (root !== null) DFS(root, '', ans);
    
    return ans;
};
```