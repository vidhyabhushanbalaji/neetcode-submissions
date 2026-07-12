class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (len(nums)==0): return False
        mySet = {nums[0]}
        for i in range(1,len(nums)):
            if (nums[i] in mySet):
                return True
            else:
                mySet.add(nums[i])
        return False