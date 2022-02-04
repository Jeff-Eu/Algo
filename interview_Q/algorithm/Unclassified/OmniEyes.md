
Use Java, Javascript, C or Python to complete the question below

1. Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
Note:
●	Your returned answers (both index1 and index2) are not zero-based.
●	You may assume that each input would have exactly one solution and you may not use the same element twice.


```python
def twoSum(arr, target):

	sz = len(arr)
	idx1 = 0
	idx2 = sz - 1

	while True:
		sm = arr[idx1] + arr[idx2]
		if sm == target:
			return [idx1, idx2]
		elif sm > target:
			idx2 -= 1
		else:
			idx1 += 1

	return [idx1, idx2]
```

2. You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.
For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.
Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.
Note:
1.	One employee has at most one direct leader and may have several subordinates.
2.	The maximum number of employees won't exceed 2000.


```python
def findImportance():
	
```

3. You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.
If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.
Operations allowed:
●	Fill any of the jugs completely with water.
●	Empty any of the jugs.
●	Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
