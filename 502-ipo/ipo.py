import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minheap=[]
        for i in range(len(profits)):
            heapq.heappush(minheap,(capital[i],profits[i]))
        
        maxheap=[]
        for _ in range(k):
            
            while minheap and minheap[0][0]<=w:
                cap,prof=heapq.heappop(minheap)
                heapq.heappush(maxheap,-prof)
        
            if not maxheap:
                break
            w+=-heapq.heappop(maxheap)
        return w
        