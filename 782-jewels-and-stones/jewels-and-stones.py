from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        val=0
        jewel_set=set(jewels)
        for ch in stones:
            if ch in jewel_set:
                val+=1
        return val
            
        