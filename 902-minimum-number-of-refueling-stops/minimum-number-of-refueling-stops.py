class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxheap=[]
        fuel=startFuel
        prev=0
        stops=0
        stations.append([target,0])
        for position,gas in stations:
            fuel-=(position-prev)
            while fuel<0:
                if not maxheap:
                    return -1
                fuel+=-heapq.heappop(maxheap)
                stops+=1
            
            heapq.heappush(maxheap,-gas)
            prev=position
        return stops
        