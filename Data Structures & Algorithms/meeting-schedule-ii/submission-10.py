"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        def sorter(x):
            return x.start
        rooms = []
        intervals.sort(key=sorter)
        
        for meeting in intervals:
            placed = False
            for i in range(len(rooms)):
                if rooms[i]<=meeting.start:
                    rooms[i] = meeting.end
                    placed=True
                    break
            if not placed:
                rooms.append(meeting.end)
        
        return len(rooms)
        """
        starts = []
        ends = []

        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()

        startpointer=0
        endpointer=0

        rooms = 0
        maxRooms = 0

        while startpointer<len(starts):
            if ends[endpointer]<=starts[startpointer]:
                rooms-=1
                endpointer+=1
            else:
                rooms+=1
                startpointer+=1
                maxRooms = max(maxRooms, rooms)
        return maxRooms
        
