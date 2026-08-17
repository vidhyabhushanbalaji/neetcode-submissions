class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]
        for i in range (len(temperatures)):
            #print(stack)                
            if len(stack)>0 and temperatures[stack[-1]]<temperatures[i]:
                while(len(stack)>0 and temperatures[stack[-1]]<temperatures[i]):
                    temp = stack.pop()
                    res[temp] = (i-temp)
            stack.append(i)
        return res

