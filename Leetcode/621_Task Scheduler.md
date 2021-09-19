# 621. Task Scheduler
Q: Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 
Example 1:
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
```
Example 2:
```
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
```
Example 3:
```
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
```
## Answer
直接看解XD

一開始看不太懂題目舉的第一個例子，後來在Leetcode論譠看到解說：

Example 1:
input: ['A', 'A', 'A', 'B', 'B', 'B'], n = 2

output: 8

A -> B -> idle -> A -> B -> idle -> A -> B

Explanation: after you do A, you have to wait two cyles for cooling time to do A again. After doing B, we also have to wait to cyles. So, the 3rd interval, we can't do A again nor B, the only option is idle. For the 4rd cyle, we can do A again since it has been at least 2 interval since the las time.

解法，利用bucket的思想就很容易了解，參考[力扣高手解](https://leetcode-cn.com/problems/task-scheduler/solution/tong-zi-by-popopop/)的說明圖，但是代碼用詳解的比較清楚。

還有上面力扣高手解的第三張圖引出的公式應該改成如下才清楚
```
總排隊時間 = (桶個數(maxExec) - 1) * (n + 1) + maxCount
```
其中
```python
maxCount = sum(1 for v in freq.values() if v == maxExec)
```

完整代碼：
```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)

        # 最多的執行次數
        maxExec = max(freq.values())
        # 具有最多執行次數的任務數量
        maxCount = sum(1 for v in freq.values() if v == maxExec)

        return max((maxExec - 1) * (n + 1) + maxCount, len(tasks))
```