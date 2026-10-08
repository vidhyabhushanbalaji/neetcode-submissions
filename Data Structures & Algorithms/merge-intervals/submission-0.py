class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def getFirst(interval):
            return interval[0]
        intervals.sort(key= getFirst)

        current = 0
        while current<len(intervals)-1:
            if intervals[current+1][0]<=intervals[current][1]:
                intervals[current]=[min(intervals[current][0], intervals[current+1][0]), max(intervals[current][1], intervals[current+1][1])]
                del intervals[current+1]
            else:
                current+=1
        return intervals