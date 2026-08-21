class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        possible = 1

        while left<=right:
            mid = (left+right)//2
            #calculate time it'd take with that
            tempSum = 0
            for i in piles:
                tempSum+= math.ceil(i/mid)
            if tempSum>h:
                left = mid+1
            else:
                possible = mid
                right = mid-1
        
        return possible