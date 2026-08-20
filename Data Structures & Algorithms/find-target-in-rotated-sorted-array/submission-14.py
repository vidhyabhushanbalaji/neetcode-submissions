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
        if target>nums[-1] and shift!=0:
            left = 0
            right = shift-1
        else:
            left = shift
            right = len(nums)-1 

        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif target>nums[mid]:
                left= mid+1
            else:
                right = mid-1
        return -1
            
