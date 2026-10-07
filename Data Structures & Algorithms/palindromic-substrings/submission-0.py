class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for mid in range(len(s)):
            left = mid
            right = mid
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                right+=1
                left-=1
            left = mid
            right = mid+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                right+=1
                left-=1
        return count
            