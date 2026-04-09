from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))
        dist=[float('inf')]*(n+1)
        dist[k]=0

        heap=[(0,k)]

        while heap:
            time,node=heapq.heappop(heap)
            if time>dist[node]:
                continue
            
            for nei,w in graph[node]:
                if time+w<dist[nei]:
                    dist[nei]=time+w
                    heapq.heappush(heap,(dist[nei],nei))
        maxtime=max(dist[1:])
        return maxtime if maxtime!=float('inf') else -1 
        
        