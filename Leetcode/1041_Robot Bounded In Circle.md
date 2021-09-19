# 1041. Robot Bounded In Circle
Q: On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

* "G": go straight 1 unit;
* "L": turn 90 degrees to the left;
* "R": turn 90 degrees to the right.
* The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:
```
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
```
Example 2:
```
Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
```
Example 3:
```
Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
```
## Answer

首刷約45分，卡在三角函數不熟，這題如果三角函數熟的話其實很簡單。

https://highscope.ch.ntu.edu.tw/wordpress/?p=51374

複習一下旋轉矩陣
```
[ CosA -SinA
  SinA Cost ]
```
上面的矩陣運算是[row major](https://stackoverflow.com/questions/32190006/android-matrix-setvalues-row-major-or-column-major)，所以點 p 用直的來表示，乘在矩陣後面。

另外複習一下映射矩陣
```
[ Cos2B  Sin2B
  Sin2B -Cos2B ]
```
B是映射線的角度，注意這裡是兩倍

* 負號位置的記法：先學旋轉才學映射矩陣，從左上角開始，按照順時針給負值 - 先學旋轉矩陣，順時針移動一格，負值在右邊；後學映射矩陣，順時針再移動一格，負值就在右下角。

另外注意python語法的陷阱，[tuple直接相加跟預期的不一樣](https://stackoverflow.com/questions/497885/python-element-wise-tuple-operations-like-sum)。

```python
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        def nextDir(d, c):
            if c=="L":
                return (-d[1], d[0])
            else: # R
                return (d[1], -d[0])
            
        p = (0, 0)
        direct = (0, 1)
        # 要加速的話，這裡可改成 *1 就先判斷相等後回傳true；若不相等再跑 *3 然後回傳是否相等 
        for c in instructions * 4:
            if c=="G":
                p = (p[0]+direct[0], p[1]+direct[1])
            else:
                direct = nextDir(direct, c)
            
        return p == (0, 0)
'''
Mr=
CosA -SinA
SinA CosA
A=90:
0 -1
1 0
A=-90:
0 1
-1 0

1 0
0 -1
'''
```