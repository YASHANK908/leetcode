class Solution(object):
    def calculate(self, s):
        stack=[]
        result=0
        num=0
        sign=1
        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch in "+-":
                result+=num*sign
                num=0
                sign=1 if ch=='+' else -1
            elif ch=='(':
                stack.append(result)
                stack.append(sign)
                result,sign=0,1
            elif ch==')':
                result+=num*sign 
                num=0
                result*=stack.pop()
                result+=stack.pop()
        return result+sign*num            
                    
        