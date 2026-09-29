class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = {len(cost):0, len(cost)+1:0}
        def climb(stair):
            if stair not in res:
                res[stair] = cost[stair]+min(climb(stair+1), climb(stair+2))
            return res[stair]
        return min(climb(0), climb(1))
