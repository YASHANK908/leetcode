from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need=Counter(s1)
        window=Counter()
        req_len=len(s1)
        left=0
        for right in range(len(s2)):
            window[s2[right]]+=1
            while right-left+1>req_len:
                window[s2[left]]-=1
                if window[s2[left]]==0:
                    del window[s2[left]]
                left+=1
            if right-left+1==req_len and window==need:
                return True
        return False
        