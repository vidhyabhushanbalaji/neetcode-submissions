class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}
        maximum = 1
        for i in nums:
            if i in vals:
                vals[i]+=1
                maximum = max(vals[i], maximum)
            else:
                vals[i]=1
        
        freqs = [[] for i in range(maximum)]

        for i in vals:
            freqs[vals[i]-1].append(i)
        
        res = []
        pointer = len(freqs)-1
        while len(res)!=k:
            for i in freqs[pointer]:
                res.append(i)
            pointer-=1
        return res