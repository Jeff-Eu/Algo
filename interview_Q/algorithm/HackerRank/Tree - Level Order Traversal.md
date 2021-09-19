# Q: https://www.hackerrank.com/challenges/tree-level-order-traversal/problem


## Answer
二刷 約16分, all pass, 有參考如何用 deque:
```python
import collections  # 記！
def levelOrder(root):
    q = collections.deque()  # 記！
    q.appendleft(root)  # 記！

    while q:
        node = q.pop() # 記！
        
        print node.info, # 注意這行每次output會用一個空格隔開
        if node.left:
            q.appendleft(node.left)
        if node.right:
            q.appendleft(node.right)
```
一刷
```python
from Queue import Queue
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
	#Write code Here
    q = Queue()
    q.put(root)
    while not q.empty():
        p = q.get()
        print p.info,
        if p.left is not None:
            q.put(p.left)
        if p.right is not None:
            q.put(p.right)
```