class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxLen =0
        charSet = {""}
        while right!= len(s):
            if s[right] in charSet:
                maxLen = max(len(charSet), maxLen)
                charSet.remove(s[left])
                left+=1

            else:
                charSet.add(s[right])
                right+=1
        return max(maxLen, len(charSet))-1