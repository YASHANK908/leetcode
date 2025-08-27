from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        need=Counter(t)
        window={}

        left,right=0,0
        valid,start=0,0
        minlen=float('inf')
        while right < len(s):
            c=s[right]
            right+=1
            if c in need:
                window[c]=window.get(c,0)+1
                if window[c]==need[c]:
                    valid+=1

            while valid == len(need):
                if right-left<minlen:
                    start=left
                    minlen=right-left
                d= s[left]
                left+=1
                if d in need:
                    if window[d]==need[d]:
                        valid-=1
                    window[d]-=1
        return "" if minlen==float('inf') else s[start:start+minlen]                        
         
        