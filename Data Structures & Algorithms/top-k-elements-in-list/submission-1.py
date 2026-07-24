class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}
        final = [[] for _ in range (len(nums))]
        count = 0
        for i in nums:
            print(i)
            if i in vals:
                vals[i]+=1
            else:
                vals[i] = 1
            count += 1

        for i,j in vals.items():
            print(i,j)
            final[j-1].append(i)
        res = []
        count = 0
        for i in range(len(final)-1, -1, -1):
            for j in final[i]:
                count+=1
                res.append(j)
                if count==k:
                    return res

        return res

