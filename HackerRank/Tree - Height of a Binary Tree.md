# Q: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

## Answer
Jeff二刷:
12分 all pass
```python
def height(root):

    def dfs(node):
        if not node:
            return 0

        a = 1 + dfs(node.left)
        b = 1 + dfs(node.right)

        return max(a,b)
    return dfs(root)-1
```

```python
maxH = 0
def height(root):
    global maxH
    dfs(-1, root)
    return maxH

def dfs(h, node):
    global maxH
    if node is None:
        return
    h+=1
    maxH = max(maxH, h)
    dfs(h, node.left)
    dfs(h, node.right)
```