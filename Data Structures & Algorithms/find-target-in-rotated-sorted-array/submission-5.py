class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)

        left = 0
        right = len(nums)-1

        mid = 0

        while left<right:
            mid = (left+right)//2
            if nums[mid]<nums[mid-1]:
                break
            elif nums[right]<nums[mid]:
                left = mid+1
            else:
                right = mid-1
        
        shift = (left+right)//2
        left = shift
        right = ((left-1)+length)%length

        virtualLeft = 0
        virtualRight = len(nums)-1

        

        while virtualLeft<=virtualRight:
            mid = (virtualLeft+virtualRight)//2
            temp = (mid+shift)%length
            if nums[temp] == target:
                return temp
            elif target>nums[temp]:
                virtualLeft= mid+1
            else:
                virtualRight = mid-1
        return -1
            
