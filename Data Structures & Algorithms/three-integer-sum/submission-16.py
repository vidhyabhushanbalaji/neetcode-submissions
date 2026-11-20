class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        
        for i in range(len(nums)):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            if nums[i]>0:
                break
            
            left = i+1
            right = len(nums)-1

            while left<right:
                sum3= nums[i]+nums[left]+nums[right]
                
                if sum3==0:
                    res.append([nums[i], nums[left], nums[right]])
                    currLeft = nums[left]
                    while left<right and nums[left]==currLeft:
                        left+=1
                elif sum3>0:
                    currRight = nums[right]
                    while left<right and nums[right]==currRight:
                        right-=1
                else:
                    currLeft = nums[left]
                    while left<right and nums[left]==currLeft:
                        left+=1
        
        return res