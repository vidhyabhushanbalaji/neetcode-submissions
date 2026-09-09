class Solution:
    def hammingWeight(self, n: int) -> int:
        curr = n
        counter = 0
        loc = 0
        while curr!=0:
            if (curr%2==1):
                counter+=1
            curr = curr//2
        return counter