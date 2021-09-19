# 146. LRU Cache
Q: Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

**Follow up:**
Could you do both operations in O(1) time complexity?

Example:
```
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

補充：這題有個沒有說清楚的地方，例如Cache容量限制為2，已存在兩個用 key,value 存的元素分別為(2, 4)及(3, 6)，這時如果要再put進(2, 5)，那在本題並不是直接更新(2, 4)後就沒事，還要仿造get的行為將它移動到最前面，而這題的範例並沒有提到這點。

## Ans

這題就算知道大致的解法，但實作時還是有很多細節需注意，像是容量限制為2的Cache分別放進 (2,6), (1,2)，這時再put進 (1,5)只會更新(1,2)成(1,5)，並不會將(2,6)剔除。

觀念：用一個hash跟一個double link list(dlist)，hash存的是 (key, dlist的node)，每一個node存的是(key, value)
```
head<->n1<->n2<->...<->tail

* List 遞增的方向是往右
* n-> 是 n.next
* <-n 是 n.prev
* 超過size會先刪head->node的node
```
* 這題如果有做過，它的解法觀念不難想起來，但是實作上，如果沒有記憶過，要在25分內寫出來不太可能，容易寫出有bug的程式，最好的方式還是記憶高手解1的寫法，特別是一些關鍵的地方：
    * 一開始有一個 head 的 node 在左邊跟 tail 的 node 在右邊，皆非空，要刪除超過size的是 head.next
    * _remove(), _add() 方法 (這兩個都是處理 linked list 的，沒處理到 dict)
        * 這兩個的參數都是 node
        * 嚴格來講這 _add() 算是 insert() ，因為最後面已經有一個 tail，它是插入至 tail.prev 
    * 在 put(self, key, value) 中，如果要 put 的 key 已經存在 dict，這裡的做法並非將 node 拔除再插入尾端，然後再去修改它的 value ；而是直接刪除該 node，並且新增一個同key的node到尾端，而且還要再做 self.dic[key] = n，這樣dic才不會取到舊的 node。這做法雖然比較耗效能，但會比較簡潔一點點(其實想想修改跟新建的差異，只差在原本node的記憶體位址是不是有改變而已，但其實key跟value都還是一樣)。
    * self.dic[key] = n 這在python修改跟創建dict的 item都是一樣的寫法，所以在這裡不用分開寫。在 java跟 kotlin又是如何呢？

* 補充：同題在 HackerRank 要求也印出 Page Fault 資訊，請參考 [GeeksForGeeks對 Page Fault 的說明](https://www.geeksforgeeks.org/program-for-least-recently-used-lru-page-replacement-algorithm/)，不過它前面的解釋圖並沒有解釋到 LRU cache 的運作方式，具體用 LRU的解釋圖如下：

    記憶體容量是 4 個 page slots，初始為空。一開始丟入 7 0 1 2後：
    ```
        舊 <-> 新
         7 0 1 2
    0 => 7 1 2 0
    3 => 1 2 0 3
    0 => 1 2 3 0
    4 => 2 3 0 4
    ```
    * 所以 Page Fault 就是記憶體找不到對應 key 的 page，才會叫 page fault；因為找不到勢必就要創建新的 page，會很耗資源，所以才需要統計 page faults 的數量。
    * 摘錄：Different page replacement algorithms suggest different ways to decide which page to replace. The target for all algorithms is to reduce number of page faults.

高手解1:
```python
# Runtime: 212 ms, faster than 89.23% of Python online submissions for LRU Cache.
# Memory Usage: 22.2 MB, less than 6.67% of Python online submissions for LRU Cache.
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            # del self.dic[key] # 這行可以省略
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n # python修改跟創建dict的 item都是一樣的寫法，所以在這裡不用分開寫。在 java跟 kotlin又是如何呢？
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key] # 注意這裡不是 dic[key] ！！

# 也可以寫成下面降可能好懂一點點
    def put2(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        elif len(self.dic) >= self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key] # 注意這裡不是 dic[key] ！！

        n = Node(key, value)
        self._add(n)
        self.dic[key] = n 

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        self.tail.prev = node
        node.next = self.tail
```

Jeff's:

跟高手解1的想法是一樣的，但是寫法卻太亂了，不值得拿來面試用；直接參考高手解1就好
```python
# Runtime: 296 ms, faster than 36.32% of Python online submissions for LRU Cache.
# Memory Usage: 22 MB, less than 40.00% of Python online submissions for LRU Cache.
class Node:
    def __init__(self, key, value):
        self.pre = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = self.tail = None
        self.dict = {}
        self.cap = capacity
        self.len = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            node = self.dict[key]
            if node.next:
                if self.head == node:
                    self.head = node.next
                
                node.next.pre = node.pre
                if node.pre:
                    node.pre.next = node.next
                
                node.pre = self.tail
                self.tail.next = node
                node.next = None
                self.tail = node
                        
            return node.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.dict:
            if self.len >= self.cap:
                del self.dict[self.head.key]

                if self.head.next:
                    self.head = self.head.next
                    self.head.pre = None
                else:
                    self.head = None
            else:
                self.len += 1

            node = self.dict[key] = Node(key, value)

            if not self.head:
                self.head = node

            if not self.tail:
                self.tail = node
            else:
                pre = self.tail
                self.tail = node
                pre.next = node
                node.pre = pre
        else:
            self.dict[key].value = value
            self.get(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

[HackerRank 類似題](https://www.hackerrank.com/contests/justcode/challenges/lru-implementtion/submissions/code/1329896474): 要處理 stdin 的資料比較麻煩，而且有兩筆 test input是最後每個數字算一行，不是全部寫成一行用空白分隔。
* 新技能，兩種讀取輸入的方式
    * `s = sys.stdin.readline()`
    * 把剩下輸入全讀進來
        ```
        s = ""
        for line in sys.stdin:
            s += line
        arr = s.split()
        ```
修改自Leetcode:
```python
import sys

class Node(object):
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache(object):
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.mp = dict()
        self.head = Node()
        self.tail = Node()
        self.size = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
        self.faults = 0

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.mp:
            self._remove(self.mp[key])
        else:
            self.faults += 1
            
        node = Node(key, value)
        self._add(node)
        self.mp[key] = node
        
        if len(self.mp) > self.size:
            n = self.head.next
            self._remove(n)
            del self.mp[n.key]
        
    def _add(self, node):
        p = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = p
        p.next = node
    
    def _remove(self, node):
        n = node.next
        p = node.prev
        p.next = n
        n.prev = p
        
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = sys.stdin.readline()
arr = s.split()
size = int(arr[1])
s = ""
for line in sys.stdin:
    s += line
arr = s.split()
data = []
for s in arr:
    data.append(int(s))
    
lru = LRUCache(size)
for d in data:
    lru.put(d, d)
    
node = lru.tail.prev

print lru.faults

while node != lru.head:
    print node.val,
    node = node.prev
```