class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = {len(cost):0, len(cost)+1:0}

        def DP(n):
            if n in res:
                return res[n]
            else:
                res[n]=cost[n]+min(DP(n+1), DP(n+2))
                return res[n]
        return min(DP(0), DP(1))