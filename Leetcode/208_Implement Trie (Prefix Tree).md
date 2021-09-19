# 208. Implement Trie (Prefix Tree)
Q: Implement a trie with insert, search, and startsWith methods.

Example:
```
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
```
Note:
* You may assume that all inputs are consist of lowercase letters a-z.
* All inputs are guaranteed to be non-empty strings.

## Answer
Leetcode 有詳解，看圖片跟code就夠理解，文字內容反而不易理解，自己實作過一遍就更懂了。另外詳解是用一個陣列去儲存 26 個英文字母，更好的解法是用一個 dictionary 存英文字母，如此可以減少初始化變數的次數，又能省記憶體。

其實Trie的實作不難，它就像 Linked List的 data structure，會有一個member連到自己的class，只是還多了一個 isEnd 的member，知道這兩個後，剩下要實作的(題目要求)方法就很容易。

看詳解後二刷(16分)
```python 3
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mp = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self
        for c in word:
            if c in trie.mp:
                trie = trie.mp[c]
            else:
                trie.mp[c] = Trie()
                trie = trie.mp[c]
                
        trie.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self
        for c in word:
            if c in trie.mp:
                trie = trie.mp[c]
            else:
                return False
            
        return trie.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self
        for c in prefix:
            if c in trie.mp:
                trie = trie.mp[c]
            else:
                return False
            
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

Jeff 看詳解後一刷:
```python
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.link = {}
        self.isEnd = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        trie = self
        for c in word:
            if c not in trie.link:
                trie.link[c] = Trie()
            trie = trie.link[c]
        trie.isEnd = True

    def prefixLink(self, word):
        trie = self
        for c in word:
            if c in trie.link:
                trie = trie.link[c]
            else:
                return None
        
        return trie
                
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        trie = self.prefixLink(word)
        
        return trie != None and trie.isEnd == True
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.prefixLink(prefix) != None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```