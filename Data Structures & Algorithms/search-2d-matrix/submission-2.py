class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        leftIndex=0
        rightIndex = len(matrix)*width-1
        midIndex=0
        while leftIndex<=rightIndex and rightIndex<=width*len(matrix)-1:
            midIndex=leftIndex+(rightIndex-leftIndex)//2
            curr = matrix[midIndex//width][midIndex%width]
            if  curr == target:
                return True
            elif target>curr:
                leftIndex = midIndex+1
            else:
                rightIndex = midIndex-1
        return False
