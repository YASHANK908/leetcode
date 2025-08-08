class Solution(object):
    def isPalindrome(self, s):
        st= ''.join(c.lower() for c in s if c.isalnum())
        left=0
        right=len(st)-1
        
        while left<right:
            if(st[left]!=st[right]):
                return False
            left+=1
            right-=1
        return True    
        