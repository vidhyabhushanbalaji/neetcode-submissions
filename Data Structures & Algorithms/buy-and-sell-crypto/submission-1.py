class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        currMin = prices[0]
        for i in prices:
            currMin = min(i, currMin)
            bestProfit = max((i-currMin), bestProfit)
        return bestProfit