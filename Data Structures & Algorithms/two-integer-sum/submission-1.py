class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myD = {nums[0]: 0}
        for i in range(1, len(nums)):
            if (target-nums[i] in myD):
                return [myD[target-nums[i]], i]
            else:
                myD[nums[i]]=i
        return[-1,-1]
