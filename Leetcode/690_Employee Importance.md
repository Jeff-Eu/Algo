# 690. Employee Importance

You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

You are given an array of employees `employees` where:

-   `employees[i].id` is the ID of the `ith` employee.
-   `employees[i].importance` is the importance value of the `ith` employee.
-   `employees[i].subordinates` is a list of the IDs of the direct subordinates of the `ith` employee.

Given an integer `id` that represents an employee's ID, return _the **total** importance value of this employee and all their direct and indirect subordinates_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/31/emp1-tree.jpg)

**Input:** employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
**Output:** 11
**Explanation:** Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3.
They both have an importance value of 3.
Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/05/31/emp2-tree.jpg)

**Input:** employees = [[1,2,[5]],[5,-3,[]]], id = 5
**Output:** -3
**Explanation:** Employee 5 has an importance value of -3 and has no direct subordinates.
Thus, the total importance value of employee 5 is -3.

**Constraints:**

-   `1 <= employees.length <= 2000`
-   `1 <= employees[i].id <= 2000`
-   All `employees[i].id` are **unique**.
-   `-100 <= employees[i].importance <= 100`
-   One employee has at most one direct leader and may have several subordinates.
-   The IDs in `employees[i].subordinates` are valid IDs.

## Answer

For fast traversing the tree, we convert the original list into a HashMap in which every element stores the following data structure,
```
key: (id: Int)
value: (importance: Int, subordinates: HashSet<id: Int>)
```
Then we can use DFS to traverse the HashMap for our target id to increment all the importance in a subtree of the id.  

```java kotlin
// Runtime: 264 ms, faster than 89.13% of Kotlin online submissions for Employee Importance.
// Memory Usage: 47.2 MB, less than 63.04% of Kotlin online submissions for Employee Importance.
/*
 *	// Definition for Employee.
 *	class Employee {
 *		var id:Int = 0
 *		var importance:Int = 0
 *		var subordinates:List<Int> = listOf()
 *	}
 */

class Solution {
    fun getImportance(employees: List<Employee?>, id: Int): Int {

        val mp = HashMap<Int, Pair<Int, HashSet<Int>>>()

        for (employee in employees) {
            val idHashSet = employee!!.subordinates.toHashSet()
            mp[employee.id] = Pair(employee.importance, idHashSet)
        }

        var ans = 0
        fun dfs(employeeID: Int) {
            
            val pair = mp[employeeID]!!
            
            ans += pair.first
            if (pair.second.isEmpty())
                return

            for (subOrdinateID in pair.second) {
                dfs(subOrdinateID)
            }
        }
        dfs(id)
        return ans
    }
}
```

```python
# Runtime: 160 ms, faster than 61.60% of Python online submissions for Employee Importance.
# Memory Usage: 15.6 MB, less than 6.91% of Python online submissions for Employee Importance.
"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        mp = dict()
        for emp in employees:
            
            # st = set()
            # for subId in emp.subordinates:
            #     st.add(subId)
            
            mp[emp.id] = (emp.importance, set(emp.subordinates))
            
        ans = [0]
        def dfs(aId):
            ans[0] += mp[aId][0]
            if len(mp[aId][1]) == 0:
                return
            
            for subId in mp[aId][1]:
                dfs(subId)
                
        dfs(id)
        return ans[0]
```
Time: O(N)
Space: O(N)
where N is the number of employees.

#medium