from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need=Counter(p)
        window=Counter()

        res=[]
        req_len=len(p)
        left=0

        for right in range(len(s)):
            window[s[right]]+=1
            while right-left+1>req_len:
                window[s[left]]-=1
                if window[s[left]]==0:
                    del window[s[left]]
                left+=1
            if right-left+1==req_len and window==need:
                res.append(left)
        return res    

        