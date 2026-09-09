class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        left = 0
        right = width*len(matrix)-1

        while left<=right:
            mid = (left+right)//2
            print(left, right)
            if matrix[mid//width][mid%width]==target:
                return True
            elif matrix[mid//width][mid%width]<target:
                left = mid+1
            else:
                right = mid-1
        return False