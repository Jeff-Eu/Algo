# Python
import Queue

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Sol:
    def listDataInSameHeightOfTree(self, root, h):
        q = Queue.Queue()
        nodesInSomeH = 0
        now_h = 0
        q.put(root) # push data to queue
        while (not q.empty()) and now_h <= h:
            now_h += 1
            nodesInSomeH = q.qsize()
            while nodesInSomeH > 0:
                node = q.get() # pop data from queue
                if node.left != None:
                    q.put(node.left)
                if node.right != None:
                    q.put(node.right)
                if now_h == h:
                    print node.data
                nodesInSomeH -= 1


# Test Data
r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)
r.right.left = Node(6)
r.right.right = Node(7)
r.left.left.left = Node(8)
r.left.left.right = Node(9)
r.left.right.left = Node(10)
r.left.right.right = Node(11)

sol = Sol()
sol.listDataInSameHeightOfTree(r, 4)