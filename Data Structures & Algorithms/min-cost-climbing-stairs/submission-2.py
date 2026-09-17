class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = {len(cost):0, len(cost)+1:0}
        def climbStairs(curr):
            if curr in res:
                return res[curr]
            else:
                res[curr]= cost[curr]+min(climbStairs(curr+1), climbStairs(curr+2))
                return res[curr]
        return min(climbStairs(0), climbStairs(1))
    
