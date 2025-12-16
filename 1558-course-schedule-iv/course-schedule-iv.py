from collections import defaultdict,deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=defaultdict(list)
        indegree=[0]*numCourses

        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v]+=1
        
        queue=deque()

        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        topo=[]

        while queue:
            node=queue.popleft()
            topo.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        
        reachable =[set() for _ in range(numCourses)]

        for u in reversed(topo):
            for v in graph[u]:
                reachable[u].add(v)
                reachable[u].update(reachable[v])
        
        return[v in reachable[u] for u,v in queries]
        