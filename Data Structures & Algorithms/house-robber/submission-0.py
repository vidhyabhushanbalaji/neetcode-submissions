class Solution:
    def rob(self, nums: List[int]) -> int:
        sols = {len(nums):0, len(nums)+1:0, len(nums)+2:0 }
        def DP(n):
            if n in sols:
                return sols[n]
            else:
                sols[n]=nums[n]+max(DP(n+2), DP(n+3))
                return sols[n]
        return max(DP(0), DP(1))
