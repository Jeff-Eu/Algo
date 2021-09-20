# 17. Letter Combinations of a Phone Number
Q: Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![src](imgs/17_1.png)

Example:
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

## Ans:
Jeff 二刷:\
Runtime: 16 ms, faster than 85.38% of Python online submissions for Letter Combinations of a Phone Number.

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 花時間的寫法
        # dic = {"2": ['a','b','c'], "3": ['d','e','f'], "4": ['g','h','i'], 
        #        "5":['j', 'k','l'], "6":['m','n','o'], "7":['p','q','r','s'],
        #       "8":['t','u','v'], "9":['w','x','y','z']}
        
        # 降寫快許多
        dic = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs",
               '8':"tuv", '9':"wxyz"}

        r = []
        if digits:
            r = dic[digits[0]]

        for i in xrange(1, len(digits)):
            n = digits[i]
            r = [c2+c1 for c1 in dic[n] for c2 in r]
        return r
```

Using Queue to implement BFS

Jeff's
```python
from Queue import Queue
dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs",
               '8':"tuv", '9':"wxyz"}
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        r = []
        queue = Queue()
        i = 0
        size = len(digits)
        curr = ""
        while True:

            if i < size:
                s = dict[digits[i]]
                for c in s:
                    queue.put(curr + c)
            else:
                r.append(curr)
                        
            if queue.empty():
                return r
            
            curr = queue.get()
            
            if len(curr) > i:
                i+=1
```