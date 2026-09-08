import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = max(piles)

        left = 1
        right = max_speed

        currMin = float("infinity")

        while left<=right:
            mid = (left+right)//2
            time_taken =0
            for i in piles:
                time_taken += math.ceil(i/mid)
            
            if time_taken > h:
                left = mid+1
            else:
                currMin = min(currMin, mid)
                right = mid-1
        
        return currMin
