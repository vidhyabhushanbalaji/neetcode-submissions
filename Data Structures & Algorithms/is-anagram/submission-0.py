from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = defaultdict(int)
        for i in s:
            d1[i]+=1
        d2 = defaultdict(int)
        for i in t:
            d2[i]+=1
        return (d2==d1)