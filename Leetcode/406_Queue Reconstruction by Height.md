# 406. Queue Reconstruction by Height
Q:Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example
```
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```
## Answer
Jeff's first (約花了30分才想到)
```python
# Runtime: 76 ms, faster than 86.22% of Python online submissions for Queue Reconstruction by Height.
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x:x[1])
        people.sort(key=lambda x:-x[0])
#       [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
        # print people
    
        size=len(people)
        
        for i in xrange(size):
            p = people.pop(i)
            people.insert(p[1], p)
            
        return people
```