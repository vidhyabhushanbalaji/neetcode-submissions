class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        first = nums[0]
        nums.pop(0)
        sols={len(nums):0, len(nums)+1:0, len(nums)+2:0}
        def DP(n):
            if n in sols:
                return sols[n]
            else:
                sols[n]=nums[n]+max(DP(n+2),DP(n+3))
                return sols[n]
        startRight = max(DP(0), DP(1))

        nums.insert(0, first)
        nums.pop(-1)
        sols={len(nums):0, len(nums)+1:0, len(nums)+2:0}
        startLeft = max(DP(0), DP(1))

        return max(startLeft, startRight)
