class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        currMax=0
        left= 0
        letters = {}
        maxfreq = 0

        for right in range(len(s)):
            letters[s[right]]= 1+ letters.get(s[right], 0)
            maxfreq = max(maxfreq, letters[s[right]])

            if (right-left+1)- maxfreq >k:
                letters[s[left]]-=1
                left+=1
            currMax = max(currMax, (right-left+1))

        return currMax
            