# 98. Validate Binary Search Tree
Q: Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:

```
Input: root = [2,1,3]
    2
  /   \
 1
Output: true
```
Example 2:

```
Input: root = [5,1,4,null,null,3,6]
     5
    /  \
  1    4
      /  \
     3    6 
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

## Answer
FAMG都出現！
Jeff首刷 19分鐘

int最大值 sys.maxint ；最小值 -sys.maxint-1 (僅在 Python 2； [Python 3移除了int最大值的限制](https://stackoverflow.com/questions/9860588/maximum-value-for-long-integer/9860611#:~:text=maxint%20The%20largest%20positive%20integer,of%202's%20complement%20binary%20arithmetic.))

float最大值 float("inf") ；最小值 float("-inf")\

解題觀念，利用 Inorder 去遍歷BST，值會從小到大排列。
```python
# Runtime: 32 ms, faster than 85.31% of Python online submissions for Validate Binary Search Tree.
# Memory Usage: 18.5 MB, less than 5.31% of Python online submissions for Validate Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        tmp = [-sys.maxint]
        
        out = [True]
        def dfs(node): # preorder
            if out[0] == False or not node:
                return
            
            dfs(node.left)
            if node.val > tmp[0]:
                tmp[0] = node.val
            else:
                out[0] = False
            dfs(node.right)
            
        
        dfs(root)
        return out[0]
```

java:(注意，因為題目有限制`-2^31 <= Node.val <= 2^31 - 1`，這代表不能用Integer去存值，就用Long取代之)
```java
// Runtime: 0 ms, faster than 100.00% of Java online submissions for Validate Binary Search Tree.
// Memory Usage: 39 MB, less than 27.36% of Java online submissions for Validate Binary Search Tree.
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        
        long[] tmp = {Long.MIN_VALUE};
        return dfs(root, tmp);
    }
    
    boolean dfs(TreeNode node, long[] tmp) {
        if(node==null) return true;
        
        if(!dfs(node.left, tmp))
            return false;
        
        if(tmp[0] >= node.val)
            return false;
        else
            tmp[0] = node.val;
            
        if(!dfs(node.right, tmp))
            return false;
        
        return true;        
    }
}
```