# 1138. Alphabet Board Path
Q: On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

![1138](imgs\1138.png)

We may make the following moves:

* 'U' moves our position up one row, if the position exists on the board;
* 'D' moves our position down one row, if the position exists on the board;
* 'L' moves our position left one column, if the position exists on the board;
* 'R' moves our position right one column, if the position exists on the board;
* '!' adds the character board[r][c] at our current position (r, c) to the answer.

(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

 

Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Example 2:

Input: target = "code"
Output: "RR!DDRR!UUL!R!"
 

Constraints:

1 <= target.length <= 100
target consists only of English lowercase letters.

## Answer
Thought: First, do Normalization. Each character on the map can be converted into a coordinate position. Then the direction from A to B is just a vector of A->B on the Cardesian Coordinate System.

For speed up the whole program, we can replace the `getCoord()` function with the memory saved dictionary. This is a kind of Dynamic Programming (DP) approach.

Jeff's first (No DP)
```python
1138. Alphabet Board Path
class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        # a=(1,2)
        # b=a
        # print b
        # a=(2,3) 
        # print b # (1, 2) 所以tuple算是一種primitive type
        
        def getCoord(c):
            diff = ord(c)-ord("a")
            x=diff%5
            y=diff/5
            return (x,y)
        
        def appendUpDown():
            s=""
            if dy>0:
                s += "D"*dy
            elif dy<0:
                s += "U"*(-dy)
            return s
            
        def action(dx, dy, isToZ):
            s=""
            if not isToZ:
                s += appendUpDown()
                
            if dx>0:
                s += "R"*dx
            elif dx<0:
                s += "L"*(-dx)
                
            if isToZ:
                s += appendUpDown()
                
            if s:
                return s+"!"
            else:
                return "!"
            
        out=""
        curr=(0,0)
        for c in target:
            last=curr
            curr=getCoord(c)
            dx=curr[0]-last[0]
            dy=curr[1]-last[1]
            out += action(dx,dy, True if c=='z' else False)
        return out
```