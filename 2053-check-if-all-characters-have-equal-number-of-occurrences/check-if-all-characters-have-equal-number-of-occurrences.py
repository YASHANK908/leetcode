from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count=Counter(s)

        if len(set(count.values()))==1:
            return True
        else:
            return False
        