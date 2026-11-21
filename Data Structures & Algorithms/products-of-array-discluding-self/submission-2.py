class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodLeft = [1]*len(nums)
        prodRight= [1]*len(nums)

        for i in range(len(nums)-1):
            prodLeft[i+1]=prodLeft[i]*nums[i]
        for i in range(len(nums)-1, 0, -1):
            prodRight[i-1]=prodRight[i]*nums[i]
        
        res = []
        for i in range(len(prodRight)):
            res.append(prodRight[i]*prodLeft[i])
        return res