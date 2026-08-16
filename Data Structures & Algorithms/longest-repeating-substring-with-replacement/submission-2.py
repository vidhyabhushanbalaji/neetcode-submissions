class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        currMax=0
        left= 0
        availiable = k
        letters = {'Q': 0, 'W': 0, 'E': 0, 'R': 0, 'T': 0, 'Y': 0, 'U': 0, 'I': 0, 'O': 0, 'P': 0, 'A': 0, 'S': 0, 'D': 0, 'F': 0, 'G': 0, 'H': 0, 'J': 0, 'K': 0, 'L': 0, 'Z': 0, 'X': 0, 'C': 0, 'V': 0, 'B': 0, 'N': 0, 'M': 0}

        for right in range(len(s)):
            letters[s[right]]+=1

            if (right-left+1)-(max(letters.values())) >k:
                letters[s[left]]-=1
                left+=1
            currMax = max(currMax, (right-left+1))

        return currMax
            