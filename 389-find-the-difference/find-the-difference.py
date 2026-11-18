from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count=Counter(s)
         
        for word in t:
            if count[word]>0:
                count[word]-=1
            else:
                return word



        