# 381. Insert Delete GetRandom O(1) - Duplicates allowed
Q: Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
* insert(val): Inserts an item val to the collection.
* remove(val): Removes an item val from the collection if present.
* getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.

Example:
```
// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
```
## Answer
首刷約花1小時

解題加速技能:
* 寫sample推理時，value乘上10，就可避免跟 index 的數字混淆, e.g.
```
mp:
21,{0,2,4}
18,{1,5}
31,{3}

ls:
21,18,21,31,21,18
```

題目380用的是 HashMap(val, index) + List，這題再進階一點，用 HashMap(val, HashSet(index)) + List

一開始以為前者要用 HashMap(val, List(index))，這想法是錯的，因為它裡面的 List的最後一個值可能不會存數值最大的(被swap之後就可能發生)

這題不好在25分內寫出，詳解的python語法比較精練，可以再練習一次

python新技能:
* 要從set中移除並取出任意一值： `item = myset.pop()` ，如果不想移除該值只想peek的寫法是 `next(iter(mp[val]))`
    * from https://stackoverflow.com/questions/59825/how-to-retrieve-an-element-from-a-set-without-removing-it
* [DefaultDict](https://www.geeksforgeeks.org/defaultdict-in-python/)

Jeff首刷:
```python
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mp = {}
        self.ls = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        mp = self.mp
        ls = self.ls
        sz = len(ls)
        if val not in mp:
            ls.append(val)
            mp[val] = set()
            mp[val].add(sz)
            return True
        else:
            ls.append(val)
            mp[val].add(sz)
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        mp = self.mp
        ls = self.ls
        szls = len(ls)
        if val in mp:
            idx = next(iter(mp[val]))
            lastVal = ls[-1]
            ls[idx] = lastVal
            ls.pop()
            
            mp[val].remove(idx)
            mp[lastVal].add(idx)
            mp[lastVal].remove(szls-1)
            if not mp[val]:
                del mp[val]
            
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return choice(self.ls)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

詳解的 code
```python
from collections import defaultdict
from random import choice

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.idx = defaultdict(set)


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.idx[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.idx[val]) == 1


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.idx[val]: return False
        remove, last = self.idx[val].pop(), self.lst[-1]
        self.lst[remove] = last
        self.idx[last].add(remove)
        self.idx[last].discard(len(self.lst) - 1)
        self.lst.pop()
    
        if not self.idx[last]: # 詳解沒加這兩行可能會造成memory leak
            del self.idx[last]
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.lst)
```