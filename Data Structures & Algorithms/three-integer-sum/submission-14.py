class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        prev=nums[0]-1
        length = len(nums)-1
        for i in range(0,len(nums)):
            curr = nums[i]
            if (curr==prev):
                continue
            if (curr>0):
                break
            
            left = i+1
            right = length
            #print(i, left, right)
            while (left<right):
                #print(i, left, right)
                negsum = -1*(nums[left]+nums[right])
                if  negsum == curr:
                    #print(i, left, right)
                    res.append([curr, nums[left], nums[right]])
                    currleft = nums[left]
                    while(nums[left]==currleft and left<right):
                        left+=1
                    curright = nums[right]
                    while(nums[right]==curright and left<right):
                        right-=1
                elif negsum<curr:
                    curright = nums[right]
                    while(nums[right]==curright and left<right):
                        right-=1
                else:
                    currleft = nums[left]
                    while(nums[left]==currleft and left<right):
                        left+=1
            prev = curr
        return res

            
