# 784. Letter Case Permutation
Q: Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

Example 1:
```
Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
```
Example 2:
```
Input: S = "3z4"
Output: ["3z4","3Z4"]
```
Example 3:
```
Input: S = "12345"
Output: ["12345"]
```
Example 4:
```
Input: S = "0"
Output: ["0"]
``` 

Constraints:
* S will be a string with length between 1 and 12.
* S will consist only of letters or digits.

## Answer
新技能:
* lower(), upper(), islower(), isupper() 可以用在 string 或 character
* character 可以直接跟 string 連接 e.g. s += c 降寫合法
* isalpha() 用在 character
* level order 的方法類似 BFS，只是它不用 queue，而是每次將新掃描的一層存進一個 list變數 L ，而不是存進 queue，然後下次就從舊 list 的每個 node 去找下一層的全部 nodes ，存進一個新創建的 list，再將它設給 L ，如此一直疊代到停為止。

```python
# Runtime: 36 ms, faster than 96.65% of Python online submissions for Letter Case Permutation.
# Memory Usage: 14.3 MB, less than 52.42% of Python online submissions for Letter Case Permutation.
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        print S
        print id(S.lower())
        print id(S)
        print S
        s = ""
        ans = [""]
        for c in S:
            if not c.isalpha(): # Number
                ans = [(subs + c) for subs in ans]
            else: # Letter
                # tmp = []
                # for subs in ans:
                #     tmp.append(subs + c.lower())
                #     tmp.append(subs + c.upper())
                # ans = tmp
                ans = [subs + cc for subs in ans for cc in [c.lower(), c.upper()]]
        return ans
```