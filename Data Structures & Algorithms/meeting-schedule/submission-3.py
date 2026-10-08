"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        starts, ends = [], []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()
        currEnd=ends[0]
        for pointer in range(1, len(ends)):
            if starts[pointer]<currEnd:
                return False
            else:
                currEnd = ends[pointer]
        return True