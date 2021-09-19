# 100. Same Tree
Q: Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:

```
Input: p = [1,2,3], q = [1,2,3]
   1
  /  \
 2    3
Output: true
```
Example 2:
```
Input: p = [1,2], q = [1,null,2]
   1       1
 /          \
2            2
Output: false
```
Example 3:
```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

## Answer
* 新技能: name list as ls

* 這題用 preorder, inorder 或 postorder 都可以
* 順便去複習一下 encode/decode tree那題

首刷約50分

python
```python
# Runtime: 16 ms, faster than 80.59% of Python online submissions for Same Tree.
# Memory Usage: 13.4 MB, less than 93.34% of Python online submissions for Same Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        out = [True]
        def dfs(n1, n2):
            if not out[0]:
                return
            if not n1 and not n2:
                return
            elif not n1 or not n2:
                out[0] = False
                return
            
            dfs(n1.left, n2.left)
            
            if n1.val != n2.val:
                out[0] = False
            
            dfs(n1.right, n2.right)
        
        dfs(p, q)
        return out[0]
```
java
```java
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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        boolean out[] = {true};
        
        dfs(p, q, out);
        return out[0];
    }
    
    void dfs(TreeNode p, TreeNode q, boolean[] out) {
        if(!out[0])
            return;
        if(p==null && q==null)
            return;
        else if(p==null || q==null) {
            out[0] = false;
            return;
        }
        
        dfs(p.left, q.left, out);
        
        if(p.val != q.val)
            out[0] = false;
        
        dfs(p.right, q.right, out);
    }
}
```
C
```C++ (C)
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void dfs(struct TreeNode* p, struct TreeNode* q, bool* pIsTrue) {
    if(*pIsTrue == false)
        return;
    
    if(p==NULL && q==NULL)
        return;
    else if((p==NULL) != (q==NULL) || p->val != q->val){ // 注意||前面的判斷要用括號，這是模擬logical xor 的寫法
        *pIsTrue=false;
        return;
    }
    
    dfs(p->left, q->left, pIsTrue);
    dfs(p->right, q->right, pIsTrue);
}

bool isSameTree(struct TreeNode* p, struct TreeNode* q){

    bool isTrue = true;
    
    dfs(p, q, &isTrue);
    
    return isTrue;
}
```