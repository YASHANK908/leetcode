from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        map1=Counter(s)
         
        for word in t:
            if map1[word]>0:
                map1[word]-=1
            else:
                return word



        