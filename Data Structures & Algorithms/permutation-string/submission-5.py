class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s2))<len(s1):
            return False

        s1=s1.upper()
        s2=s2.upper()

        s1Map = {'Q': 0, 'W': 0, 'E': 0, 'R': 0, 'T': 0, 'Y': 0, 'U': 0, 'I': 0, 'O': 0, 'P': 0, 'A': 0, 'S': 0, 'D': 0, 'F': 0, 'G': 0, 'H': 0, 'J': 0, 'K': 0, 'L': 0, 'Z': 0, 'X': 0, 'C': 0, 'V': 0, 'B': 0, 'N': 0, 'M': 0}
        s2Map= s1Map.copy()

        for i in range (len(s1)):
            s1Map[s1[i]]+=1
            s2Map[s2[i]]+=1

        left = 0
        right = len(s1)-1

        while (right<len(s2)-1):
            print("---")
            for i in s2Map:
                if s2Map[i]>0: print(i)
            if s1Map == s2Map:
                return True
            else:
                print()
                s2Map[s2[left]]-=1
                s2Map[s2[right+1]]+=1
                left+=1
                right+=1
        
        return (s1Map==s2Map)
        

