"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()
    
        currStart = 0
        currEnd = 0
        while currStart<len(starts)-1:
            if starts[currStart+1]<ends[currEnd]:
                return False
            currStart+=1
            currEnd+=1
        return True