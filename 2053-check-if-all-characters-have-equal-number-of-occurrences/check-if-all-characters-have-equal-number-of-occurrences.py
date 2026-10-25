from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count=Counter(s)
    
        return min(count.values())==max(count.values())
        