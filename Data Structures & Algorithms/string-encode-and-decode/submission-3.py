class Solution:

    def encode(self, strs: List[str]) -> str:
        together = "".join(strs)
        nums = ""
        for i in strs:
            nums = nums + str(len(i))+","
        return (nums + "-" + together)
    
    def decode(self, s: str) -> List[str]:
        print(s)
        nums = []
        words = []
        temp = ""
        rem = -1
        for i in range (len(s)):
            if (s[i]==","):
                nums.append(int(temp))
                temp = ""
            elif (s[i]=="-"):
                rem = i+1
                break
            else:
                temp = temp+s[i]
        word = 0
        count = 0
        temp = ""
        pointer = 0

        for i in nums:
            if i == 0:
                words.append("")
            else:
                while count < i:
                    temp = temp+ s[rem]
                    rem+=1
                    count+=1
                words.append(temp)
                temp = ""
                count = 0
        
        return words
            