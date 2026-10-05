class Solution:
    def longestConsecutive(self, nums):
        starts = {}
        ends= {}
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                continue
            if (i-1) in ends and (i+1) in starts:
                starts[i-ends[i-1]]+= (1 + starts[i+1])
                ends[i+starts[i+1]] = starts[i-ends[i-1]]
            elif (i+1) in starts:
                ends[i+starts[i+1]]+=1
                starts[i] = starts[i+1]+1
            elif (i-1) in ends:
                starts[i-ends[i-1]]+=1
                ends[i]=ends[i-1]+1
            else:
                starts[i]=1
                ends[i]=1
        maxim = 0
        for i in starts:
            maxim= max(maxim, starts[i])
        return maxim