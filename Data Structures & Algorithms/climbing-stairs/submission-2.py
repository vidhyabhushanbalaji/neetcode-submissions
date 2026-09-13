class Solution:
    def climbStairs(self, n: int) -> int:
        sols = {-1:1, 0:1, 1:1}
        def DP(n):
            if n in sols:
                return sols[n]
            else:
                sols[n]=DP(n-1)+DP(n-2)
                return sols[n]
        return DP(n)