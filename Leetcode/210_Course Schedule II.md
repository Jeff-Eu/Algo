# 210. Course Schedule II
Q: There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```
Example 2:
```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
```
Example 3:
```
Input: numCourses = 1, prerequisites = []
Output: [0]
```

## Answer
近似於 207. Course Schedule

```python
# Runtime: 80 ms, faster than 71.66% of Python online submissions for Course Schedule II.
# Memory Usage: 14.9 MB, less than 70.12% of Python online submissions for Course Schedule II.
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
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
                    
        if len(tOrder) != size:
            return []
        else:
            return tOrder 
```