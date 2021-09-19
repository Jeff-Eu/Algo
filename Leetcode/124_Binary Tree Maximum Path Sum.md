# 124. Binary Tree Maximum Path Sum
Q: Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:
```
Input: root = [1,2,3]
    1
  /   \
 2     3
Output: 6
```
Example 2:
```
Input: root = [-10,9,20,null,null,15,7]
    -10
    /  \
   9    20
        / \
       15  7
Output: 42
```
## Answer
[這論譠講解的非常好](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/shou-hui-tu-jie-hen-you-ya-de-yi-dao-dfsti-by-hyj8/)

補充:
* 這題要拿一張白紙來畫圖才容易理解。
* 這題的最佳解其實也有隱藏 DP 的觀念，我在下面java的解法註解的部分中，本來想用 getMaxWithNode() 來求解，看似好理解，但會重覆遞迴的計算沒利用到 DP，速度就慢很多。
    * 那裡用到DP？ 因為 maxOnePathWithNode() 這函式行的通，而裡面的遞迴本身也會遍歷樹的每一個node，因此可順搭上這個特性去找我們要的最大值。
    * [觀念] 這個 maxOnePathWithNode() 的遍歷就是程式的核心，即First Principle，不能沒有它，接著就思考是否能在不添加額外遍歷樹的函式的情況下，能重覆利用它來達到最少的計算。
* 對於dfs來說的三種，其實說穿了都是去找 left及 right
    * 承上，所以算法中會去掃 traverse 每一個 node，在求最終的 maxSum時，{ maxSum的組成，是存在於 tree中任意一個 node，"往左往右任意延伸的一筆畫路徑" -> 令作 outputPath} -> 令作 innerPath，這 outputPath 的和要愈大愈好，並傳給 parent做總和，但若這 outputPath 的和形成負數，parent 就不需要把這條 outputPath 加進去他本身去組合成 innerPath，所以下面的 code才會 `return max(outputMaxSum, 0)`，若在白紙上畫出所有可能的 innerPath ，就可以歸納出所有 innerPath 的形狀都長成 / 或 \ 或 倒V形，或是一個點，記得都是一筆劃不會重覆的路徑。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxSum = [-sys.maxint]
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 下面這兩行只是為了求題目要的解，但若拿掉這兩行，題目可以變成問，由任意node延伸到下面的任何路徑(一筆劃)，求最大和的那條路徑
            innerMaxSum = left + node.val + right
            maxSum[0] = max(maxSum[0], innerMaxSum)
            
            outputMaxSum = node.val + max(left, right)
            
            return max(outputMaxSum, 0)
        
        dfs(root)
        return maxSum[0]
```

Kotlin
```java kotlin
class Solution {
    fun maxPathSum(root: TreeNode?): Int {
        var maxSum = -Int.MIN_VALUE
        
        fun dfs(node: TreeNode?): Int {
            if(node == null)
                return 0

            var left = dfs(node.left)
            var right = dfs(node.right)

            var innerMaxSum = left + node.`val` + right
            maxSum = maxOf(maxSum, innerMaxSum)

            var outputMaxSum = node.`val` + maxOf(left, right)
            return maxOf(outputMaxSum, 0)
        }
        dfs(root)
        
        return maxSum
    }
}
```
```java
// Runtime: 0 ms, faster than 100.00% of Java online submissions for Binary Tree Maximum Path Sum.
// Memory Usage: 40.7 MB, less than 85.76% of Java online submissions for Binary Tree Maximum Path Sum.
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
    public int maxPathSum(TreeNode root) {
        
        int[] r = { Integer.MIN_VALUE };
        // System.out.println(Math.max(-3, 7));
        maxOnePathWithNode(root, r);
        return r[0];
    }
    
    // if minus, return 0
    int maxOnePathWithNode(TreeNode node, int[] r) {
        if (node==null)
            return 0;
        
        int v = node.val;
        int lmax = maxOnePathWithNode(node.left, r);
        int rmax = maxOnePathWithNode(node.right, r);
        
        int mx = node.val + lmax + rmax;
        if(mx > r[0])
            r[0] = mx;
        return Math.max(0, v + Math.max(lmax, rmax));
    }
    
//     void getMaxWithNode(TreeNode node, int[] r){
//         if(node==null)
//             return;
        
//         int ml = maxOnePathWithNode(node.left, r);
//         int mr = maxOnePathWithNode(node.right, r);
        
//         int mx = node.val + ml + mr;
//         if (mx > r[0])
//             r[0]=mx;
        
//         getMaxWithNode(node.left, r);
//         getMaxWithNode(node.right, r);        
//     }
}
```