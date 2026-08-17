class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+", "-", "*", "/"}
        stack = []
        for i in tokens:
            if i in operands:
                if i=="+":
                    var1 = stack.pop()
                    var2 = stack.pop()
                    stack.append(var1+var2)
                elif i=="*":
                    var1 = stack.pop()
                    var2 = stack.pop()
                    stack.append(var1*var2)
                elif i=="-":
                    var1 = stack.pop()
                    var2 = stack.pop()
                    stack.append(var2-var1)
                else:
                    var1 = stack.pop()
                    var2 = stack.pop()
                    stack.append(int(var2/var1))
            else:
                stack.append(int(i))
        return(stack[-1])