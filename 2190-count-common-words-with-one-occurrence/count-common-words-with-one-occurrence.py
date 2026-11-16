from collections import Counter
class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        map1=Counter(words1)
        map2=Counter(words2)
        result=0
        for word in words1:
            if word in map2 and map1[word]==1 and map2[word]==1:
                result+=1
        return result 

        