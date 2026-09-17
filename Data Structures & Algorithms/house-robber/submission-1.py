class Solution:
    def rob(self, nums: List[int]) -> int:
        res = {len(nums):0, len(nums)+1:0, len(nums)+2:0,}
        def houseRobber(curr):
            if curr not in res:
                res[curr] = nums[curr]+max(houseRobber(curr+2), houseRobber(curr+3))
            return res[curr]
        return max(houseRobber(0), houseRobber(1))