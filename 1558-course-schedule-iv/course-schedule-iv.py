from collections import defaultdict,deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=defaultdict(list)
        inDegree=[0]*numCourses
        prereq=[set() for _ in range(numCourses)]

        for u,v in prerequisites:
            graph[u].append(v)
            inDegree[v]+=1

        q= deque([i for i in range(numCourses) if inDegree[i]==0])

        while q:
            node=q.popleft()
            for nei in graph[node]:
                prereq[nei].update(prereq[node])
                prereq[nei].add(node) 
                inDegree[nei]-=1
                if inDegree[nei]==0:
                    q.append(nei)
        return [u in prereq[v] for u,v in queries]               

        