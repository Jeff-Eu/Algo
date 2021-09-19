# 211. Add and Search Word - Data structure design
Q: Design a data structure that supports the following two operations:
```
void addWord(word)
bool search(word)
```
search(word) can search a literal word or a regular expression string containing only letters `a-z` or `.`. A `.` means it can represent any one letter.

Example:
```
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
```
Note:
You may assume that all words are consist of lowercase letters `a-z`.

## Answer
這題是難在 search 時，可使用題目表示的萬用字元 `.`來搜尋單字，因此為了要遍歷整個樹，勢必離不開遞迴的寫法，事實上是 backtracking 的觀念。 

Jeff 不限時首刷 (Time: 74.74%, Space: 34.69%)
```python
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.link = {}
        self.isEnd = False

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        trie = self
        for c in word:
            if c not in trie.link:
                trie.link[c] = WordDictionary()
            trie = trie.link[c]
        trie.isEnd = True
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def track(i, trie):
            if isFind[0]:
                return
            elif i == size:
                if trie.isEnd:
                    isFind[0] = True
                return
            
            if word[i] == '.':
                for k in trie.link:
                    track(i+1, trie.link[k])
            elif word[i] in trie.link:
                track(i+1, trie.link[word[i]])    
            
        isFind = [False]
        i = 0
        size = len(word)
        track(i, self)
        
        return isFind[0]
```