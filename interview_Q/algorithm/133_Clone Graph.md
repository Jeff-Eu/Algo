# 133. Clone Graph
Q: Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:

```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
```
Example 2:

```
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
```
Example 3:
```
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
```
Example 4:

```
Input: adjList = [[2],[1]]
Output: [[2],[1]]
``` 

Constraints:
* 1 <= Node.val <= 100
* Node.val is unique for each node.
* Number of Nodes will not exceed 100.
* There is no repeated edges and no self-loops in the graph.
* The Graph is connected and all nodes can be visited starting from the given node.

## Answer
[Youtube DFS solution](https://www.youtube.com/watch?v=e5tNvT1iUXs) 介紹:
```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        dic = {}
        
        def cloneNode(node):
            if node.val in dic:
                return dic[node.val]
            copy = Node(node.val, [])
            dic[node.val] = copy
            for nei in node.neighbors:
                copy.neighbors.append(cloneNode(nei))    
            return copy
        
        if not node:
            return None
        else:
            return cloneNode(node)
```

Jeff's BFS solution (500) (99.18%)\
這方法是花了一些時間自己想到的，一開始卡在queue到底append會不會造成重覆，後來才感知到不會重覆的append方式。
```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        dic = {}
        q = deque()
        q.append(node)
        
        def bfs(copy, n):
            for nei in n.neighbors:
                if nei.val in dic:
                    copy2 = dic[nei.val]
                else:
                    q.append(nei)  # Only here to append an element to queue
                    copy2 = Node(nei.val, [])
                    dic[nei.val] = copy2
                copy.neighbors.append(copy2)
        
        while q:
            n = q.pop()
            if n.val not in dic:
                copy = Node(n.val, [])
                dic[n.val] = copy
            else:
                copy = dic[n.val]
            bfs(copy, n)
        
        return dic[node.val]
```