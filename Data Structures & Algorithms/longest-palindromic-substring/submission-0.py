class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_palin = ""
        for mid in range(len(s)):
            left = mid
            right = mid
            while left>=0 and right<len(s):
                if s[right]==s[left]:
                    right+=1
                    left-=1
                else:
                    break
            right-=1
            left+=1
            if right-left+1>len(best_palin):
                best_palin = s[left:right+1]
            left = mid
            right = mid+1
            while left>=0 and right<len(s):
                if s[right]==s[left]:
                    right+=1
                    left-=1
                else:
                    break
            right-=1
            left+=1
            if right-left+1>len(best_palin):
                best_palin = s[left:right+1]
        return best_palin