class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxLen =0
        charSet = set()
        x = len(s)
        while right!= x:
            if s[right] in charSet:
                maxLen = max(right-left, maxLen)
                charSet.remove(s[left])
                left+=1
            else:
                charSet.add(s[right])
                right+=1
        return max(maxLen, right-left)