from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        
        graph=[[] for _ in range(n) ]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
       
        visited=set()

        q=deque([source])
        visited.add(source)

        while q:
            node=q.popleft()
            if node==destination:
                return True
            
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return False
                
        