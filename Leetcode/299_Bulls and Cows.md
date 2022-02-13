# 299. Bulls and Cows
Q: You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:
```
Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
```
Example 2:
```
Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
```
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

## Answer
高手解:
```python
class Solution(object):
    def getHint(self, secret, guess):
        bull, cow = 0, 0
        s = {} # secret hashtable
        g = {} # guess hashtable
        
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                s[secret[i]] = s.get(secret[i], 0) + 1
                g[guess[i]] = g.get(guess[i], 0) + 1
        
        for k in s:
            if k in g:
                cow += min(s[k], g[k])
        
        return '{0}A{1}B'.format(bull, cow)
```
看過高手解後一刷:
```python
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        N = len(secret)
        a = b = 0
        s = {}
        g = {}
        for x, y in zip(secret, guess):
            if x == y:
                a += 1
            else:
                s[x] = s.get(x, 0) + 1
                g[y] = g.get(y, 0) + 1
        
        for n in s:
            if n in g:
                b += min(s[n], g[n])
                
        return "%sA%sB" % (a, b)
```