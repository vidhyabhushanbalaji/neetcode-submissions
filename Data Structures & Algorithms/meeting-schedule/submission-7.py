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
        def function(meeting):
            return meeting.start
        intervals.sort(key=function)

        for pointer in range(1, len(intervals)):
            if intervals[pointer].start<intervals[pointer-1].end:
                return False
        return True