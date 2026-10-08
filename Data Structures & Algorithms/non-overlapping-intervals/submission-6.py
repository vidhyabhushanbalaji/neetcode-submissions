class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def sortFunc(interval):
            return interval[0], -1*interval[1]
        intervals.sort(key=sortFunc)
        currEnd = intervals[0][0]
        deletes = 0
        for i in range(len(intervals)):
            if intervals[i][0]<currEnd:
                currEnd = min(currEnd, intervals[i][1])
                deletes+=1
            else:
                currEnd = intervals[i][1]
        return deletes