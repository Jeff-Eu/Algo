# 151. Reverse Words in a String
Q: Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

## Answer
Jeff 抽象化快速解:
先用下面這個快速解法，若面試官要求再把函式實作出來 divide and conquer !
```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split()
        return " ".join(arr[::-1])
```

In place 高手解:

First, reverse the whole string, then reverse each word.
```c++
void reverseWords(string &s) {
    reverse(s.begin(), s.end());
    int storeIndex = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] != ' ') {
            if (storeIndex != 0) s[storeIndex++] = ' ';
            int j = i;
            while (j < s.size() && s[j] != ' ') { s[storeIndex++] = s[j++]; }
            reverse(s.begin() + storeIndex - (j - i), s.begin() + storeIndex);
            i = j;
        }
    }
    s.erase(s.begin() + storeIndex, s.end());
```

Jeff's answer(一般解):
```python
class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):

        i = 0
        state = 0
        size = len(A)
        arr = []
        s = ""
        while i < size:
            if state == 0:
                if A[i] != ' ':
                    state = 1
                    s += A[i]
            else:
                if A[i] == ' ':
                    arr.append(s)
                    s = ""
                    state = 0
                else:
                    s += A[i]
            i += 1
        
        if i >= 1 and A[i-1] != ' ':
            arr.append(s)

        i = len(arr) - 1
        out = ""
        while i >= 0:
            if i != 0:
                out += arr[i] + " "
            else:
                out += arr[i]
            i -= 1

        return out
```