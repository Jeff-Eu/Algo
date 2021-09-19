# 380. Insert Delete GetRandom O(1)
Q: Design a data structure that supports all following operations in average O(1) time.

1. insert(val): Inserts an item val to the set if not already present.
2. remove(val): Removes an item val from the set if present.
3. getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

Example:
```
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
```

## Answer
做這題會聯想起 146. LRU Cache，但解法完全不同，這題用的是 HashMap + List；而146題用的是 HashMap + LinkedList。

本題解法的核心思路(from [論譠](https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85425/Java-Solution-(Beats-99.20)-Using-HashMap-and-ArrayList-with-Explanation)):\
The main trick is when you remove a value. ArrayList's remove method is O(n) if you remove from random location. To overcome that, we swap the values between (randomIndex, lastIndex) and always remove the entry from the end of the list. After the swap, you need to update the new index of the swapped value (which was previously at the end of the list) in the map.

實作上這題比146稍簡單，不像 146會有陷阱要避免。

理解後，6小時候後複刷 (約30分)
```python
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mp = {}
        self.ls = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.mp:
            return False
        else:
            self.mp[val] = len(self.ls)
            self.ls.append(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.mp:
            idx = self.mp[val]
            ls = self.ls
            last = ls[-1]
            # 因為ls[-1]終究會被刪除，之後可以不用管ls[-1]的值是多少，因此下面這行可簡化為 ls[idx] = ls[-1] 就好
            ls[idx], ls[-1] = ls[-1], ls[idx]
            self.mp[last] = idx
            ls.pop()
            del self.mp[val]
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # v = random.randint(0, len(self.ls)-1)
        # return self.ls[v]
        # 等同上面兩行
        return choice(self.ls)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

若還是想不起來可參考[力扣高手說明](https://leetcode-cn.com/problems/insert-delete-getrandom-o1/solution/chang-shu-shi-jian-cha-ru-shan-chu-he-huo-qu-sui-j/)

Python新技能：
```python
import random

random.randint(3, 9)  # 3~9隨機取一值

choice(ls) # 從ls隨機取一個元素 (ls是一個List)
```