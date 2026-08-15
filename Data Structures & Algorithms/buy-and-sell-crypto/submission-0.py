class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        currMin = prices[0]
        for i in prices:
            if (i<currMin):
                currMin=i
            if (i-currMin)>bestProfit:
                bestProfit = i-currMin
        return bestProfit