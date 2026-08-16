class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxLen =0
        charSet = {" "}
        charSet.remove(" ")
        while right!= len(s):
            #print(left, right, maxLen, charSet)
            if s[right] in charSet:
                maxLen = max(len(charSet), maxLen)
                charSet.remove(s[left])
                currChar = s[right]
                left+=1
                #while (s[left]==currChar) and left<right:
                #    left+=1
            else:
                charSet.add(s[right])
                right+=1
        return max(maxLen, len(charSet))