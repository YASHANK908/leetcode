class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=len(s)
        sa=0
        
        for i in range(n-1,-1,-1):
            if s[i]!=" ":
                sa+=1
            elif sa>0:
                return sa
        return sa
        

        