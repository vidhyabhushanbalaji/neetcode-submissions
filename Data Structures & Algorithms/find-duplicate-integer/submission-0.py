class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fullRange = set(range(1,len(nums)))
        for i in nums:
            try:
                fullRange.remove(i)
            except:
                return i
        
