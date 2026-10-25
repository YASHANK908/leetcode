class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count={}

        for ch in s:
            count[ch]=count.get(ch,0)+1
        
        for ch in t:
            if count.get(ch,0)>0:
                count[ch]-=1
            else:
                return ch
        