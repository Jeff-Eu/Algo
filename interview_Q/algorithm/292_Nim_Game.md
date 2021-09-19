# 292. Nim Game
Q: You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

[Problem link](https://leetcode.com/problems/nim-game/description/)

## Hints
If there are 5 stones in the heap, could you figure out a way to remove the stones such that you will always be the winner?

## Ans

Jeff's answer:\
這題一開始覺得很怪，不懂它所謂的 _每個人都有最佳策略來贏這場遊戲_ 是什麼意思, 本來以為可能是騙人的，因為也有可能某個n的數字輸入誰都不一定會贏，在上班的交通時間憑空想也想不出來，後來看了它的hints，才在文字檔上記錄從1開始每個人贏的可能性，假設我用 true 代表換誰就誰贏，false代表換誰就誰輸，null代表未知，則：

假設一開始是自己先拿\
n=1, true\
n=2, true\
n=3, true\
n=4, false\
n=5, true\
n=6, true\
n=7, true\
n=8, false\
n=9, true\
‧‧‧


```
n=4 時，
因為拿掉1,2或3個後，決定權變對方的同時，對方的n就變成往上的三種情形，因為這三種情形對方會以最佳策略執行(全拿)來獲勝，所以自己一定會輸

n=5 時，
同樣拿掉1,2或3個後，決定權變對方的同時，對方的n就變成往上的三種情形(n=4, n=3 或 n=2)，為了讓對方變成必輸的狀態，我們只能讓對方進入 n=4，也就是自己拿走一塊，如此我們一定會贏

n=8 時，
因為無論自己拿1, 2或3塊，變成往上的三種情形，對方都能必勝，所以我們一定會輸
```
觀察以上情形，可以發現自己會輸的情形是每4個一循環，故程式就簡單變成
```python
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        else:
            return True
```