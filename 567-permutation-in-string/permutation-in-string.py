from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need=Counter(s1)
        window={}
        req=len(s1)
        left=0
        for right in range(len(s2)):
            c=s2[right]
            window[c]=window.get(c,0)+1

            while right-left+1>req:
                window[s2[left]]-=1
                if window[s2[left]]==0:
                    del window[s2[left]]
                left+=1
            if right-left+1==req and window==need:
                return True
        return False
   
   
        