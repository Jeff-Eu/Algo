# 230. Kth Smallest Element in a BST
Q: Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:
```
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
```
Example 2:
```
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
```
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

 

Constraints:

* The number of elements of the BST is between 1 to 10^4.
* You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

## Answer
Jeff複刷 (用到BST的性質)
```python 3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Using L-V-R of DFS to traverse the BST, so the order of traversal can go from minimum to maximum.
        def dfs(node):
            if not node:
                return

            if count[0] == k:
                return

            dfs(node.left)

            count[0] += 1
            if count[0] == k:
                ans[0] = node.val
                return
            
            dfs(node.right)

        count = [0]
        ans = [-1]
        dfs(root)

        return ans[0]
```


Jeff's first solution
```python
import heapq
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        heap = []
        
        def dfs(n):
            if not n:
                return
            heapq.heappush(heap, n.val)
            dfs(n.left)
            dfs(n.right)
            
        
        dfs(root)
            
        for _ in xrange(k):
            r = heapq.heappop(heap)
        return r
```