import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        
        for num,count in freq.items():
            heapq.heappush(heap,(count,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [item[1] for item in heap]
        