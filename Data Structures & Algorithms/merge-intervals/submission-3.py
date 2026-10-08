class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def getFirst(item):
            return item[0]
        intervals.sort(key=getFirst)

        current = 0
        while current<len(intervals)-1:
            if intervals[current+1][0]<=intervals[current][1]:
                intervals[current][1] = max(intervals[current][1], intervals[current+1][1])
                del intervals[current+1]
            else:
                current +=1
        return intervals