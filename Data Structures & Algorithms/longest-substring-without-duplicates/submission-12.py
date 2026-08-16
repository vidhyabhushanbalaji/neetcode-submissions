class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxLen =0
        charSet = set()
        while right!= len(s):
            if s[right] in charSet:
                maxLen = max(right-left, maxLen)
                charSet.remove(s[left])
                left+=1

            else:
                charSet.add(s[right])
                right+=1
        return max(maxLen, len(charSet))