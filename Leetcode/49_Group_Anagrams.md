# 49. Group Anagrams
Q: Given an array of strings, group anagrams together.

Example:
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```
Note:

* All inputs will be in lowercase.
* The order of your output does not matter.

## Answer
二刷
```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            # 注意 sorted(word)會產生list而非字串，用str即可將之轉成字串
            key = str(sorted(word))

            if key not in dic:
                dic[key] = []
                dic[key].append(word)
            else:
                dic[key].append(word)

        out=[]
        for key, value in dic.items():
            out.append(value)

        return out
```

Jeff's
```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        d = {}
        for s in strs:
            # 注意這會產生list而非字串
            so = sorted(s)
            # 要將list再轉回字串
            sso = str(so)
            if sso in d:
                d[sso].append(s)
            else:
                d[sso] = [s]
            
        out = []
        # 要記熟iterate dictionary的方式
        for key, val in d.items():
            out.append(val)
            
        return out
```

學平's
要判斷兩字串是不是anagrams，只要把字串排序過後再比較即可。

```javascript
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    var map = {};
    var length = strs.length;
    var result = [];
    
    for (var i = 0; i < length; i++) {
        var word = strs[i].split('').sort().join('');
        
        if (!map[word]) {
            map[word] = [];
        }
        map[word].push(strs[i]);
    }
    
    for (var key in map) {
        map[key].sort();
        result.push(map[key]);
    }
    
    return result;
};
```