class Solution:
    def longestConsecutive(self, nums):
        starts = {}
        ends = {}
        maxim = 0

        for x in nums:
            if x in starts or x in ends:
                next
            elif (x-1) in ends and (x+1) in starts:
                total_length = ends[x-1]+starts[x+1]+1
                starts[x-ends[x-1]] = total_length
                ends[x+starts[x+1]] = total_length
                maxim = max(total_length, maxim)
            elif (x+1) in starts:
                ends[x+starts[x+1]]+=1
                starts[x] = ends[x+starts[x+1]]
                maxim = max(starts[x], maxim)
            elif (x-1) in ends:
                starts[x-ends[x-1]]+=1
                ends[x]=starts[x-ends[x-1]]
                maxim = max(ends[x], maxim)
            else:
                starts[x]=1
                ends[x]=1
                maxim = max(1, maxim)
    
        return maxim
        
            