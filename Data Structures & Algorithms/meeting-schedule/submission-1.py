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
        pointer = 0
        currTime = 0
        while pointer<len(intervals):
            if starts[pointer]<currTime:
                return False
            else:
                currTime = ends[pointer]
                pointer+=1
        return True