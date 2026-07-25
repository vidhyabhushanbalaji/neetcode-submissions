class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodleft = [1]*(len(nums))
        for i in range(1, len(nums)):
            prodleft[i] = prodleft[i-1]*nums[i-1]
        temp = 1
        print(prodleft)
        for i in range(len(nums)-1, -1, -1):
            prodleft[i] = prodleft[i]*temp
            temp = temp * nums[i]
        return (prodleft)

        