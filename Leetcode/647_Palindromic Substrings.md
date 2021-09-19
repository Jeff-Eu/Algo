# 647. Palindromic Substrings
Q: Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
```
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

Example 2:
```
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
``` 

Note:

The input string length won't exceed 1000.

## Answer
前一晚看懂詳解的方法後，今早嘗試自己刷，但超過40分還是一直有錯誤，下面是大概花了一小時候成功的寫法(不建議)。
```python
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """        # Odd case
        for i in xrange(size):
            for width in xrange((size+1)/2):
                if i-width < 0 or i+width >= size:
                    break
                if s[i-width] == s[i+width]:
                    count += 1
                else:
                    break
        
        # Even case
        for i in xrange(size):
            for width in xrange(size/2):
                if i-width < 0 or i+width+1 >= size:
                    break
                if s[i-width] == s[i+width+1]:
                    count += 1
                else:
                    break
                    
        return count
```

* 去看詳解的 Approach #3: Expand Around Possible Centers ，就能比較快回想起來較好的解法。

複雜度: O(N^2)

其實上面的寫法不好，測驗時容易出包，後來瞄了一下詳解的寫法，它是另外再寫一個函式就能同時處理 Odd 跟 Even 的情況，然後我又再用類似的方法重寫一次，結果是花了十分鐘寫出。

```python
# Runtime: 100 ms, faster than 89.63% of Python online submissions for Palindromic Substrings.
# Memory Usage: 13.5 MB, less than 68.35% of Python online submissions for Palindromic Substrings.
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        size = len(s)
        count = 0
        
        def countPal(left, right):
            c = 0
            while left >= 0 and right < size:
                if s[left] == s[right]:
                    c += 1
                    left -= 1
                    right += 1
                else:
                    break
            return c
            
        # Odd
        for i in xrange(size):
            count += countPal(i, i)
            
        # Even
        for i in xrange(size):
            count += countPal(i, i+1)
            
        return count
```

論譠解
```c++
class Solution {
public:
    void checkOutwards(string &s, int &n, int left, int right,int &counter){
        while(left>=0 && right<n && s[left--]==s[right++])
                counter++;
    }
    int countSubstrings(string s) {
        int n = s.length();
        int counter=0;
        for(int i=0;i<n;i++){
            checkOutwards(s,n,i,i,counter);
            checkOutwards(s,n,i,i+1,counter);
        }
        return counter;
    }
};
```
看完論譠解後隔日刷
```c++
class Solution {
public:
    void calculateExpansion(int& sz, string& s, int& count, int left, int right) {
        while(left>=0 && right<sz && s[left] == s[right]) {
            count++;
            --left;
            ++right;
        }
    }
    
    int countSubstrings(string s) {
        int sz = s.length();
        int count = 0;
        for(int i=0; i<sz; i++) {
            calculateExpansion(sz, s, count, i, i);
            calculateExpansion(sz, s, count, i, i+1);
        }
        
        return count;
    }
};
```