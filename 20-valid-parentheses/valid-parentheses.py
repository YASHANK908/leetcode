class Solution:
    def isValid(self, s: str) -> bool:
        charmaps={')':'(',']':'[','}':'{'}
        
        stack=[]
        for i in range(len(s)):
            if s[i] in charmaps.values():
                stack.append(s[i])
            elif s[i] in charmaps :
                if not stack or stack[-1]!=charmaps[s[i]]:
                    return False
                stack.pop()
        return not stack
                


            
                    
            
             
        