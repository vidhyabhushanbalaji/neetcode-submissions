class Solution:
    def longestConsecutive(self, nums):
        starts = {}
        ends = {}
        maxLen=0

        for x in nums:
            length = 1
            if (x-1) in ends and (x+1) in starts:
                start = (x-1)-(ends[x-1])+1
                end  = (x+1)+starts[x+1]-1
                length = end-start+1
                starts[start]=length
                ends[end]=length
            elif (x-1) in ends:
                start = (x-1)-(ends[x-1])+1
                ends[x]=ends[x-1]+1
                ends.pop(x-1)
                starts[start]+=1
                length = starts[start]
            elif (x+1) in starts:
                end = (x+1)+(starts[x+1])-1
                starts[x]=starts[x+1]+1
                starts.pop(x+1)
                ends[end]+=1
                length = ends[end]
            elif x not in starts and x not in ends:
                ends[x]=1
                starts[x]=1
            maxLen=max(maxLen, length)

        return maxLen
        