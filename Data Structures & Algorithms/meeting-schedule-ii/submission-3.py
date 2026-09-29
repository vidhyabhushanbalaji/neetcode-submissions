"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        currUsed = 0
        maxUsed = 0

        startPointer = 0
        endPointer = 0

        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()

        while startPointer<len(intervals):
            if starts[startPointer]<ends[endPointer]:
                currUsed+=1
                maxUsed = max(currUsed, maxUsed)
                startPointer+=1
            elif starts[startPointer]>ends[endPointer]:
                currUsed-=1
                endPointer+=1
            else:
                startPointer+=1
                endPointer+=1
        
        return maxUsed