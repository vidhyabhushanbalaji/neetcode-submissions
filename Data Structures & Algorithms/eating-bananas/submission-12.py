import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = max(piles)

        left = 1
        right = max_speed
        potential = -1

        while left<=right:
            mid = (left+right)//2
            time_taken=0
            for i in piles:
                time_taken+=math.ceil(i/mid)
            
            if time_taken<=h:
                potential = mid
                right = mid-1
            else:
                left=mid+1
        
        return potential