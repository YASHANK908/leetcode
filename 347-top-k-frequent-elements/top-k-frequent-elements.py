from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count=Counter(nums)

        num_sor=sorted(count,key=count.get,reverse=True)
        return num_sor[:k]
        