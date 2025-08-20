import heapq
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        maxheap=[]
        fuel=startFuel
        ans=0
        prev=0
        for pos,cap in stations +[(target,0)]:
            fuel-=(pos-prev)
            while maxheap and fuel<0:
                fuel+=-heapq.heappop(maxheap)
                ans+=1
            if fuel<0:
                return -1
            heapq.heappush(maxheap,-cap)
            prev=pos
        return ans    
        