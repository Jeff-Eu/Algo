# 339 Nested List Weight Sum (付費解鎖題)
Given a nested list of integers, return the sum of all integers in the list weighted by their depth. Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example
Example 1:
```
Input: the list [[1,1],2,[1,1]], 
Output: 10. 
Explanation:
four 1's at depth 2, one 2 at depth 1, 4 * 1 * 2 + 1 * 2 * 1 = 10
```
Example 2:
```
Input: the list [1,[4,[6]]], 
Output: 27. 
Explanation:
one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4 * 2 + 6 * 3 = 27
```
## Answer
Jeff's (DFS)
```python
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        
        def dfs(nestedList, depth):
            for item in nestedList:
                if item.isInteger():
                    s[0] += item.getInteger()*depth
                else:
                    dfs(item.getList(), depth+1)
        # 注意s=[0]這個技巧，若直接以s當整數變數，在nested function會產生python獨特的錯誤
        # 1. https://stackoverflow.com/questions/2609518/unboundlocalerror-with-nested-function-scopes
        # 2. https://stackoverflow.com/questions/5218895/python-nested-functions-variable-scoping
        s = [0]
        dfs(nestedList, 1)
        return s[0]
```

學平's

這題考depth first search的概念

* 迴圈遍歷時遇到 nested list 則做DFS並且計算depth
* 迴圈遍歷時遇到 interger 則 sum += depth * integer

### Approach #1 Depth first search [Accepted]
```javascript
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * function NestedInteger() {
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     @return {boolean}
 *     this.isInteger = function() {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     @return {integer}
 *     this.getInteger = function() {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds, if it holds a nested list
 *     Return null if this NestedInteger holds a single integer
 *     @return {NestedInteger[]}
 *     this.getList = function() {
 *         ...
 *     };
 * };
 */
/**
 * @param {NestedInteger[]} nestedList
 * @return {number}
 */
var depthSum = function(nestedList) {
    var sum = 0;
    
    var DFS = function(list, depth) {
        for (var j = 0; j < list.length; j++) {
            if (list[j].isInteger()) {
                sum += depth * list[j].getInteger();
            } else {
                DFS(list[j].getList(), depth + 1);
            }
        }
    };
    
    for (var i = 0; i < nestedList.length; i++) {
        if (nestedList[i].isInteger()) {
            sum += nestedList[i].getInteger();
        } else {
            DFS(nestedList[i].getList(), 2);
        }
    }
    
    return sum;
    
};
```

### Approach #2 Depth first search [Accepted]
```java
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer,
 *     // rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds,
 *     // if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds,
 *     // if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public int depthSum(List<NestedInteger> nestedList) {
    return depthSum(nestedList, 1);
}

public int depthSum(List<NestedInteger> list, int depth) {
    int sum = 0;
    for (NestedInteger n : list) {
        if (n.isInteger()) {
            sum += n.getInteger() * depth;
        } else {
            sum += depthSum(n.getList(), depth + 1);
        }
    }
    return sum;
}
```