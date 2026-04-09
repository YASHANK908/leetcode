from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=defaultdict(list)

        for u,v,w in flights:
            graph[u].append((v,w))
        
        heap=[(0,src,0)]
        
        visited=dict()
        while heap:
            cost,node,stops=heapq.heappop(heap)
            if node==dst:
                return cost
            
            if stops>k:
                continue
            
            if node in visited and visited[node]<=stops:
                continue
            
            visited[node]=stops

            for nei,price in graph[node]:
                heapq.heappush(heap,(cost+price,nei,stops+1))
        return -1

        