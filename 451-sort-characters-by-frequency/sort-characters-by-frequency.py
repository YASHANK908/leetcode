from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        chars = sorted(count, key=count.get,reverse=True)

        result=""

        for ch in chars:
            result+=ch*count[ch]
        return result

        