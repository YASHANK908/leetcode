from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        val=0
        for ch in stones:
            if ch in jewels:
                val+=1
        return val
            
        