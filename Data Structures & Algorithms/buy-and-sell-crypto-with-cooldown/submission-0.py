class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = {}

        def DP(day, buying):
            if (day, buying) in profit:
                return profit[(day, buying)]
            if day>=len(prices):
                return 0
            
            cooldown = DP(day+1, buying)
            if buying:
                buy = DP(day+1, False) - prices[day]
                profit[(day, buying)]=max(cooldown, buy)
            else:
                sell = DP(day+2, True) + prices[day]
                profit[(day, buying)]=max(cooldown, sell)

            return profit[(day, buying)]
        
        return DP(0, True)