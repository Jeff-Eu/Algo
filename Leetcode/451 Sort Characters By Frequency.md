# 451. Sort Characters By Frequency

Given a string `s`, sort it in decreasing order based on the frequency of characters, and return *the sorted string*.

**Example 1:**

```
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

```

**Example 2:**

```
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

```

**Example 3:**

```
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

```

**Constraints:**

- `1 <= s.length <= 5 * 105`
- `s` consists of English letters and digits.

## Answer

Jeff一刷

```python
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = collections.Counter(s)
        heap = []
        r = ""
# method 1: Using heap
#         for key in dic:
#             heapq.heappush(heap, (-dic[key], key))
        
#         while heap:
#             pair = heapq.heappop(heap)
#             # for _ in xrange(-pair[0]):
#             #     # r = ''.join((r, pair[1]))
#             r += -pair[0] * pair[1]

# method 2: sort dictionary
        pairs = sorted(dic.items(), key=lambda pair: -pair[1]) # 加上負號的 -pair[1] 是為了 descending
        for key, value in pairs:
            r += key * value
                
        return r
```

注意: python中要建立連續 N 個 'a' 字元的字串，要用 N * 'a'，不要用 for迴圈 result += 'a'，或是for迴圈 ''.join((result, 'a'))，這兩個都會慢很多。

Java版

```java
class Solution {
    public String frequencySort(String s) {
        // Count the occurence on each character
        HashMap<Character, Integer> cnt = new HashMap<>();
        for (char c : s.toCharArray()) {
            cnt.put(c, cnt.getOrDefault(c, 0) + 1);
        }

        // Sorting
        List<Character> chars = new ArrayList(cnt.keySet());
        Collections.sort(chars, (a, b) -> (cnt.get(b) - cnt.get(a)));

        // Build string
        StringBuilder sb = new StringBuilder();
        for (Character c : chars) {
            for (int i = 0; i < cnt.get(c); i++) {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
```