class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)
        options = range(1, maximum+1)
        left = 0
        right = maximum-1
        possible = 1

        while left<=right:
            mid = (left+right)//2
            #calculate time it'd take with that
            tempSum = 0
            for i in piles:
                tempSum+= (i//options[mid])
                if (i%options[mid]!=0):
                    tempSum+=1
            if tempSum>h:
                left = mid+1
            else:
                possible = options[mid]
                right = mid-1
        
        return possible