class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s2))<len(s1):
            return False

        s1Map = {'q': 0, 'w': 0, 'e': 0, 'r': 0, 't': 0, 'y': 0, 'u': 0, 'i': 0, 'o': 0, 'p': 0, 'a': 0, 's': 0, 'd': 0, 'f': 0, 'g': 0, 'h': 0, 'j': 0, 'k': 0, 'l': 0, 'z': 0, 'x': 0, 'c': 0, 'v': 0, 'b': 0, 'n': 0, 'm': 0}
        s2Map= s1Map.copy()

        for i in range (len(s1)):
            s1Map[s1[i]]+=1
            s2Map[s2[i]]+=1

        left = 0
        right = len(s1)-1

        while (right<len(s2)-1):
            if s1Map == s2Map:
                return True
            else:
                print()
                s2Map[s2[left]]-=1
                s2Map[s2[right+1]]+=1
                left+=1
                right+=1
        
        return (s1Map==s2Map)
        

