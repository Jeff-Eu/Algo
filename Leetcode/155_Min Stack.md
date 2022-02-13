# 155. Min Stack
Q: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* getMin() -- Retrieve the minimum element in the stack.
 

Example 1:
```
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]

Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
``` 

Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.


## Answer
這題主要有兩種解法，分別是用兩個stack及一個stack，[這位youtuber有詳解](https://www.youtube.com/watch?v=WxCuL3jleUA)，他推薦用兩個stack的解法，比較容易懂也較易debug。

我想補充另一點，這題乍看之下可能會想用Heap去解，但Heap的insert跟delete都是O(logN)，心理反爾想怎麼可能有比Heap還好的演算法？但其實這題的演算法隱藏著一大缺點，就是它的pop是跟一般stack一樣只會pop掉最後面的元素，但最後面的元素不一定是最小的元素，不像Heap的每次delete都是刪掉最小的元素，所以這演算法只能找到目前最小的，但次小的或次次小的卻不一定能得到，所以它沒辦法取代 Heap。

Jeff知道解法後一刷:
```python
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.minStack or self.minStack[-1] >= x:
            self.minStack.append(x)
            
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.minStack and self.minStack[-1] == self.stack[-1]:
            self.minStack.pop()
        
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```