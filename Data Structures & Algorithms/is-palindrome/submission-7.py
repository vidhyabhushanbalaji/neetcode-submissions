class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        right = len(s)-1
        left = 0
        while left<=right:
            while not (s[left].isalnum()) and left<right:
                left+=1
            while not (s[right].isalnum()) and left<right:
                right-=1
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True