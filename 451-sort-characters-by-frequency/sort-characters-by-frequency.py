from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        result=""
        sorted_char=sorted(count,key=count.get,reverse=True)
        for ch in sorted_char:
            result+=ch*count[ch]

        return result

        