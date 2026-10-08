class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def getFirst(interval):
            return interval[0]

        intervals.sort(key=getFirst)
        latest = intervals[0][0]
        changes = 0

        for i in intervals:
            if i[0]<latest:
                changes+=1
                latest = min(latest, i[1])
            else:
                latest=i[1]
        return changes