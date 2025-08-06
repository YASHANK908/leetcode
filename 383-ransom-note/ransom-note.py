from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        rancount=Counter(ransomNote)
        magcount=Counter(magazine) 
        for char,freq in rancount.items():
            if magcount[char]<freq:
                return False
        return True    
        