# 692. Top K Frequent Words
Q: Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
```
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
```
Example 2:
```
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
```
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

## Study

* Python如何針對object的排序寫operator => [使用 \_\_lt\_\_ 及 \_\_eq\_\_](https://stackoverflow.com/questions/48313301/python-sort-has-higher-priority-for-lt-than-gt/48313338#48313338)

* 注意下面第一個loop
```python
n = len(lista)
for _ in xrange(n):
```
比下面這個要快得多
```python
i = 0
while i < len(lista):
    i += 1
```
* 要了解 heap 的資料結構，[可以參考這部影片](https://www.youtube.com/watch?v=HqPJF2L5h9U)
    * full binary tree的高度是 2^(h+1) - 1 , 其中 h 是樹的高度從0開始算
    * heap 一定要是 complete binary tree
    * complete binary tree的高是是 log N
    * insert 跟 delete 一個元素的複雜度都是 O(log N)
    * insert 全部元素建立出 heap 時間總共是 O(N log N)
    * delete heap內全部的元素，花的時間總共是 O(N log N)；因為每刪除一個元素可放到尾巴變成 sorted 過的序列，所以全部刪除放到尾巴就會形成一個 sorted array，總共時間就會是 insert all + delete all 的時間，即 2* O(N log N) = O(N log N)
    * heap 可以做出 priority queue
    * heap 雖然是樹的資料結構，但一般都是用陣列來表示，才有快速計算的作用
    * heap 的高度就是比較的次數，可用來計算時間複雜度
    * heapify 是將一個non-heap的陣列變成heap，只使用 O(n)的時間；比一個個insert的方法總共要 O(nlogn)的時間還要再快

## Answer
二刷輔助刷(推)
```python
# Runtime: 40 ms, faster than 82.13% of Python online submissions for Top K Frequent Words.
# Memory Usage: 13.6 MB, less than 80.86% of Python online submissions for Top K Frequent Words.
import collections
import heapq
class Solution:
    # Time Complexity = O(MlogM) # M is the number of different words
    # Space Complexity = O(N)
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # O(N)
        count = collections.Counter(words)
        heap = []
        # O(MlogM) # M is the number of different words
        for key, value in count.items():
            heapq.heappush(heap, Word(value, key))

        res = []
		# k * O(logM) # 條件有說不同字的數量 >= k
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word < other.word
        return self.freq > other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word
```

Kotlin
```java kotlin
class Solution {
    fun topKFrequent(words: Array<String>, k: Int): List<String> {
        val result = LinkedList<String>()

        val map = HashMap<String, Int>()
        for (i in words.indices) {
            if (map.containsKey(words[i]))
                // https://stackoverflow.com/questions/42705761/kotlin-map-with-non-null-values/42705954
                map[words[i]] = map.getValue(words[i]) + 1
            else
                map[words[i]] = 1
        }
        val pq = PriorityQueue<Map.Entry<String, Int>> { a, b ->
            if (a.value == b.value)
                a.key.compareTo(b.key)
            else
                b.value - a.value
        }
        for (entry in map.entries) {
            pq.offer(entry)
        }
        for (i in 1..k)
            if (!pq.isEmpty())
                result.add(pq.poll().key)

        return result
    }
}
```

## Not Good
論譠最hot解(不推，有點脫褲放屁的寫法) (Leetcode也有詳解分析複雜度):
```python
import collections
import heapq
class Solution:
    # Time Complexity = O(n + nlogk)
    # Space Complexity = O(n)
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # O(n)
        count = collections.Counter(words)
        heap = []
        # O(nlogk)
        for key, value in count.items():
            heapq.heappush(heap, Word(value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1]

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word
```