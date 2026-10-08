class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def sort_func(interval):
            return interval[0]
        intervals.sort(key=sort_func)

        removed = 0
        currEnd= intervals[0][0]
        
        for i in intervals:
            if i[0]<currEnd:
                currEnd=min(currEnd, i[1])
                removed+=1
            else:
                currEnd = i[1]
        return removed