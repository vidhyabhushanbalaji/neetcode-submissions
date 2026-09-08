"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()

        startPointer = 0
        endPointer = 0

        currInUse = 0
        currMax = 0

        while startPointer<len(starts):
            if starts[startPointer]<ends[endPointer]:
                currInUse+=1
                currMax = max(currMax, currInUse)
                startPointer+=1

            elif starts[startPointer]==ends[endPointer]:
                startPointer+=1
                endPointer+=1

            else:
                currInUse-=1
                endPointer+=1
        
        return currMax

