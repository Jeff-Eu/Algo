# Merge Overlapping Intervals
# 解說圖: http://res.cloudinary.com/yoyoyo3/image/upload/v1496483519/P_20170603_172422_unjmhl.jpg

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        result = []
        for i in intervals:
            result = self.insert(result, i)
        return result


    def insert(self, inList, newItem):
        outList = []
        isNewAdded = False
        for interval in inList:
            s = self.intersect(newItem.start, interval)
            e = self.intersect(newItem.end, interval)
            
            if s < 0:
                outList.append(interval)
            elif s == 0:
                outList.append(newItem)
                newItem.start = interval.start
                isNewAdded = True
            else:
                if isNewAdded == False:
                    outList.append(newItem)
                    isNewAdded = True

            if e == 0:
                newItem.end = interval.end
            elif e > 0:
                outList.append(interval)

        if isNewAdded == False:
            outList.append(newItem)

        return outList

    '''
        return 
        -1: interval is before pos
         0: interval covers the pos
         1: interval is after pos
    '''
    def intersect(self, pos, interval):
        if interval.end < pos:
            return -1
        elif interval.start > pos:
            return 1
        else:
            return 0


p1 = Interval(1,2)
myList = [p1]
sol = Solution()
res = sol.merge(myList)
print res
