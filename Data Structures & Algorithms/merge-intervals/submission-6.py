class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def func(interval):
            return interval[0]
        intervals.sort(key=func)

        prevEnd = intervals[0][0]-1

        pointer = 0
        while pointer<len(intervals):
            if intervals[pointer][0]<=prevEnd:
                prevEnd = max(intervals[pointer][1], prevEnd)
                intervals.pop(pointer)
                intervals[pointer-1][1] = prevEnd
            else:
                prevEnd = intervals[pointer][1]
                pointer+=1
        return intervals
