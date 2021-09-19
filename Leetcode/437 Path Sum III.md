# 437. Path Sum III

Q: You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
```

## Answer

這題在雖然是寫easy，實際上它的基本解就已經有medium的程度，若是最佳解則有hard的難度，[Leetcode有高手詳解](https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)。Leetcode論譠上有人說這題跟 560. Subarray Sum Equals K 很像。下面為截取高手的詳解

### 2. Memorization of path sum: O(n)

2.1 High level walk through

1. In order to optimize from the brutal force solution, we will have to think of a clear way to memorize the intermediate result. Namely in the brutal force solution, we did a lot repeated calculation. For example 1->3->5, we calculated: 1, 1+3, 1+3+5, 3, 3+5, 5.
2. This is a classical 'space and time tradeoff': we can create a dictionary (named cache) which saves all the path sum (from root to current node) and their frequency for the current status (The current status here means current position. The dictionary's contents change through different current positions, we'll see that soon in the code. ).
3. Again, we traverse through the tree, at each node, we can get the currPathSum (from root to current node). If within this path, there is a valid solution, then there must be a oldPathSum such that currPathSum - oldPathSum = target.
4. We just need to add the frequency of the oldPathSum to the result.
5. During the DFS break down, we need to -1 in cache[currPathSum], because this path is not available in later traverse.
6. Check the graph below for easy visualization.

    ![437%20Path%20Sum%20III%209ced23f09aeb4d1996c610c7db9f88c3/437.png](437%20Path%20Sum%20III%209ced23f09aeb4d1996c610c7db9f88c3/437.png)

2.2 Complexity analysis:

1. Space complexity O(n) extra space
2. Time complexity O(n) as we just traverse once

2.3 Code:

```python
class Solution(object):
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0:1}
        
        # recursive to get result
        self.dfs(root, target, 0, cache)
        
        # return result
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return  
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1
```

Jeff看懂答案後一刷:

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def pathSum(self, root, target):
        
        dic = {0:1}
        def dfs(node, s):
            if not node:
                return
            
            s += node.val
            old = s - target  # 註1
            out[0] += dic.get(old, 0)
            dic[s] = dic.get(s, 0) + 1
            
            dfs(node.left, s)
            dfs(node.right, s)
            dic[s] -= 1
            
        out = [0]
        dfs(root, 0)
        return out[0]
```

註1：你可能會想說這段 code的 target所包含的路徑中，會不會有重覆的？答案是不會，我們借用前面的圖說明：

![437%20Path%20Sum%20III%209ced23f09aeb4d1996c610c7db9f88c3/437.png](437%20Path%20Sum%20III%209ced23f09aeb4d1996c610c7db9f88c3/437.png)

target是 C-D 這段，s是 Root-D，而 old是 Root-B。因為在 Tree中，Root往下到任一個node的path都會是唯一的，因此 Root-D 跟 Root-B這兩條 path 都會是唯一，而 Root-B 屬於 Root-D的一部分，因此剩下的 path，也就是 C-D 也會是唯一，所以這方法才行的通；舉一個相反的例子，假設這不是一顆 Tree而是一個Graph，然後有另外一個看起來像 root的 node K指向 A，這時候會造成 target的路徑變成兩個重覆的了，所以題目一定要是 Tree這方法才有效。 

再舉一個反例，假設 old是 Root-A，然後 target 把它變成 B-C，也就是沒有連接到 D，這時候可以想像在 general 的例子中 B-C 會被很多條 path 經過，所以不是經過的 path都可以拿來算 B-C，否則會算到很多重覆的，我們要找到只需算一次 unique path 的方法，上一段就是一種方法。