"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts, ends= [], []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()

        startPointer = 0
        endPointer = 0
        curr = 0
        maxUsed = 0

        while startPointer<len(starts):
            if starts[startPointer]<ends[endPointer]:
                curr+=1
                maxUsed= max(maxUsed, curr)
                startPointer+=1
            elif ends[endPointer]<starts[startPointer]:
                curr-=1
                endPointer+=1
            else:
                startPointer+=1
                endPointer+=1
        return maxUsed