class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        starts = {}
        ends = {}
        for i in nums:
            if ((i-1) in ends) and ((i+1) in starts):
                newLength = ends[i-1] + 1 + starts[i+1]
                starts[i-1-ends[i-1]+1] = newLength
                ends[starts[i+1]+i+1-1] = newLength
            elif ((i-1) in ends):
                starts[i-1-ends[i-1]+1]+=1
                ends[i]=ends[i-1]+1
            elif((i+1) in starts):
                ends[i+1+starts[i+1]-1]+=1
                starts[i]=starts[i+1]+1
            elif not(i in starts or i in ends):
                starts[i]=1
                ends[i]=1
        max = 0
        for i in ends:
            if ends[i]>max:
                max = ends[i]
        return max