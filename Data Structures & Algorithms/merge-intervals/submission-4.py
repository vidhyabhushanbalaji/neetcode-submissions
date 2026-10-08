class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def sort_func(interval):
            return interval[0]
        current = 0
        intervals.sort(key=sort_func)
        print(intervals)
        while current<len(intervals)-1:

            if intervals[current+1][0] <= intervals[current][1]:
                intervals[current][1]=max(intervals[current][1], intervals[current+1][1])
                del intervals[current+1]
            else:
                current+=1
        return intervals