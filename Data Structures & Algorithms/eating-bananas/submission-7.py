class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)
        left = 1
        right = maximum
        possible = 1

        while left<=right:
            mid = (left+right)//2
            #calculate time it'd take with that
            tempSum = 0
            for i in piles:
                tempSum+= (i//mid)
                if (i%mid!=0):
                    tempSum+=1
            if tempSum>h:
                left = mid+1
            else:
                possible = mid
                right = mid-1
        
        return possible