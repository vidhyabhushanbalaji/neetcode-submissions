class Solution:
    def rob(self, nums: List[int]) -> int:
        sols = {len(nums):0, len(nums)+1:0, len(nums)+2:0}

        def DP(house):
            if not (house in sols):
                sols[house] = nums[house] + max(DP(house+2), DP(house+3))
            return sols[house]
        
        return max(DP(0), DP(1))