class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        pointer = 0
        while pointer<len(nums):
            for i in range(len(res)):
                res.append(res[i].copy())
                res[-1].append(nums[pointer])
            pointer+=1
        return res