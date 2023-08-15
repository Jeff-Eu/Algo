[1007. Minimum Domino Rotations For Equal Row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/)

In a row of dominoes, `tops[i]` and `bottoms[i]` represent the top and bottom halves of the `ith` domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the `ith` domino, so that `tops[i]` and `bottoms[i]` swap values.

Return the minimum number of rotations so that all the values in `tops` are the same, or all the values in `bottoms` are the same.

If it cannot be done, return `-1`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/14/domino.png)

**Input:** tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
**Output:** 2
**Explanation:** 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

**Example 2:**

**Input:** tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
**Output:** -1
**Explanation:** 
In this case, it is not possible to rotate the dominoes to make one row of values equal.

**Constraints:**

- `2 <= tops.length <= 2 * 104`
- `bottoms.length == tops.length`
- `1 <= tops[i], bottoms[i] <= 6`

## Answer

Jeff's solution (too many lines, not good)
```python
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        t = tops[0]
        b = bottoms[0]
        sz = len(tops)
        topCount = 0
        sameCount = 0
        # go through top
        for i in range(1, sz):
            if t == tops[i]:
                if t == bottoms[i]:
                    sameCount += 1
            elif t == bottoms[i]:
                topCount += 1
            else:
                topCount = -1
                break

        if (topCount != -1) and (sz-sameCount < topCount*2):
            topCount = sz-sameCount-topCount

        # go throught bottom
        bCount = 0
        sameCount = 0
        for i in range(1, sz):
            if b == bottoms[i]:
                if b == tops[i]:
                    sameCount += 1
            elif b == tops[i]:
                bCount += 1
            else:
                bCount = -1
                break

        if bCount != -1 and sz-sameCount < bCount * 2:
            bCount = sz-sameCount-bCount

        if topCount == -1:
            return bCount
        else:
            if bCount != -1:
                return min(topCount, bCount)
            else:
                return topCount
```

# 高手解

https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/solutions/252242/java-c-python-different-ideas/

### Intuition

One observation is that, if `A[0]` works, no need to check `B[0]`.  
Because if both `A[0]` and `B[0]` exist in all dominoes,  
when you swap `A[0]` in a whole row,  
you will swap `B[0]` in a whole at the same time.  
The result of trying `A[0]` and `B[0]` will be the same.  
  
### Solution 1:

Count the occurrence of all numbers in `A` and `B`,  
and also the number of domino with two same numbers.

Try all possibilities from 1 to 6.  
If we can make number `i` in a whole row,  
it should satisfy that `countA[i] + countB[i] - same[i] = n`

Take example of  
`A = [2,1,2,4,2,2]`  
`B = [5,2,6,2,3,2]`

`countA[2] = 4`, as `A[0] = A[2] = A[4] = A[5] = 2`  
`countB[2] = 3`, as `B[1] = B[3] = B[5] = 2`  
`same[2] = 1`, as `A[5] = B[5] = 2`

We have `countA[2] + countB[2] - same[2] = 6`,  
so we can make 2 in a whole row.

Time `O(N)`, Space `O(1)`


**python**

```python
    def minDominoRotations(self, A, B):
        for x in [A[0],B[0]]:
            if all(x in d for d in zip(A, B)):
                return len(A) - max(A.count(x), B.count(x))
        return -1
```


#medium 