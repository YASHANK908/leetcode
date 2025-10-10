from collections import defaultdict,deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph=defaultdict(list)
        inDegree=[0]*n
        anc=[set() for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            inDegree[v]+=1

        q=deque([i for i in range(n) if inDegree[i]==0])

        while q:
            node=q.popleft()
            for nei in graph[node]:
                anc[nei].update(anc[node])
                anc[nei].add(node)
                inDegree[nei]-=1
                if inDegree[nei]==0:
                    q.append(nei) 
        return [sorted(list(an)) for an in anc]           
        