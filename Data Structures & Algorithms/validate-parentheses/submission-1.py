class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = {"(":")", "[":"]", "{":"}"}
        closes = {")", "]", "}"}
        for i in s:
            if i in opens:
                stack.append(opens[i])
            elif len(stack)==0 or stack[-1]!= i:
                return False
            else:
                stack.pop()
        return (len(stack))==0
