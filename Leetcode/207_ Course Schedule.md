# 207. Course Schedule
Q: There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
```
Example 2:
```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
``` 

Constraints:
* The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about [how a graph is represented](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs).
* You may assume that there are no duplicate edges in the input prerequisites.
* 1 <= numCourses <= 10^5

## Answer
同 210. Course Schedule II
1/13 看過以下教學後首刷，約40分

圖論經典問題，請參考
* [圖形的資料結構表示法](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs)
* [Find Topological Ordering - Kahn's Algorithm](https://www.youtube.com/watch?v=cIBFEhD77b4)
* [番外篇，看看就好](http://web.ntnu.edu.tw/~algo/DirectedAcyclicGraph.html#:~:text=%E3%80%8C%E6%8B%93%E6%92%B2%E6%8E%92%E5%BA%8F%E3%80%8D%E6%98%AF%E6%8E%92%E5%BA%8F%E4%B8%80,%E4%B8%80%E5%80%8B%E9%BB%9E%E7%9A%84%E5%85%88%E5%BE%8C%E9%A0%86%E5%BA%8F%E3%80%82)

注意，
* 這裡 python 的 initialize
* deque 的 popleft, appendleft, extendleft 的 left 都是小寫。
* deque 若要當作是純 queue ，那你可以選擇要往左或往右 pop：
    * 往左 pop 的queue: popleft, append
    * 往右 pop 的queue: pop, appendleft 

```python
# Runtime: 76 ms, faster than 78.49% of Python online submissions for Course Schedule.
# Memory Usage: 14.8 MB, less than 85.07% of Python online submissions for Course Schedule.
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # simplify name
        size = numCourses
        graph = []
        for _ in xrange(size):
            graph.append([])
        
        # simplify name
        req = prerequisites
        
        # build adjacency list
        for pair in req:
            graph[pair[1]].append(pair[0])
        
        # calculate in-degree values for each node onto inArr
        inArr = [0]*size
        for ls in graph:
            for v in ls:
                inArr[v] += 1
                
        q = deque()
        for i in xrange(size):
            if inArr[i] == 0:
                q.append(i)
        
        tOrder = []
        while q:
            p = q.popleft()
            tOrder.append(p)
            for v in graph[p]:
                inArr[v] -= 1
                if inArr[v] == 0:
                    q.append(v)
        
        return len(tOrder) == size
```        