class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        for tok in tokens:
            if tok not in "+-*/":
                stack.append(int(tok))
            else:
                b=stack.pop()
                a=stack.pop()
                if tok=='+':
                    stack.append(a+b)
                elif tok=='-':
                    stack.append(a-b)
                elif tok=='*':
                    stack.append(a*b)
                else:
                    stack.append(int(float(a)/b))
        return stack[0]                    