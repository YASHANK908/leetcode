class Solution(object):
    def calculate(self, s):
        stack=[]
        num=0
        sign='+'
          
        for i,ch in enumerate(s):
            if ch.isdigit():
                num=num*10+int(ch)
            if ch in '+-*/'or i==len(s)-1:
                if sign=='+':
                    stack.append(num)
                elif sign=='-':
                    stack.append(-num)
                elif sign=='*':
                    stack.append(stack.pop() *num)
                elif sign=='/':
                    top=stack.pop()
                    stack.append(int(float(top)/num))  
                num=0
                sign=ch
        return sum(stack)          


        