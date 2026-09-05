class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        pointer = 0
        while pointer<len(nums):
            for i in range(len(res)):
                temp = res[i].copy()
                temp.append(nums[pointer])
                res.append(temp)
            pointer+=1
        return res