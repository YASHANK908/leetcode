class Solution(object):
    def minWindow(self, s, t):
        c_t=Counter(t)
        window_count={}
        need=len(c_t)
        req=0
        left= 0
        minlen=float('inf')
        res=""
        for right in range(len(s)):
            char=s[right]
            window_count[char]=window_count.get(char,0)+1
            if char in c_t and window_count[char]==c_t[char]:
                req+=1
            while req==need:
                if right-left+1<minlen:
                    minlen=right-left+1
                    res=s[left:right+1] 
                leftchar=s[left]
                window_count[leftchar]-=1
                if leftchar in c_t and window_count[leftchar]<c_t[leftchar]:
                    req-=1
                left+=1    
        return res if minlen!=float('inf') else "" 
         
        