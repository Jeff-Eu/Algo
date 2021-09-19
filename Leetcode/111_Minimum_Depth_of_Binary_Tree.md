# 111. Minimum Depth of Binary Tree
Q: Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

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
這題考depth first search的概念

## Answer
Jeff's DFS 解
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node.left and not node.right:
                return 1

            a=b=99999
            if node.left:
                a = dfs(node.left)
            if node.right:
                b = dfs(node.right)
            return 1+min(a,b)

        if not root:
            return 0
        
        return dfs(root)
```

後記:
* 我覺得這題用BFS去解才會有最佳解，像104題求最深的depth則DFS跟BSF都沒差
* BFS有最佳解的原因是，只要判斷為葉結點，亦即，左右子樹皆空，那該結點就是最短路徑的葉結點了，就終止繼續判斷

* I think the best solution for this problem is to use BFS, while the problem No.104 which is to find the greatest depth doesn't differ for getting fastest solution in DFS and BFS.
* There is a best solution for BFS is because you just need to get the first leaf node, i.e., left and right of the node are both empty. That node is the end of the shortest path. Then you can stop the later check.

學平's
* minimum depth初始值設為無窮大
* 從 root 開始做DFS, 並把計算出的depth與 minimum depth做比較, 取較小的數值

## Approach #1 Depth first search [Accepted]
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
var minDepth = function(root) {
    var minDepth = Number.POSITIVE_INFINITY;
    
    var DFS = function(node, depth) {
        if (node.left === null && node.right === null) minDepth = Math.min(depth, minDepth);
        if (node.left !== null) DFS(node.left, depth + 1);
        if (node.right !== null) DFS(node.right, depth + 1);
    }
    
    if (root === null) return 0;
    
    DFS(root, 1);
    
    return minDepth;
};
```