from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        result=[]

        while q:
            node=q.popleft()
            result.append(node)

            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return result if len(result)==numCourses else []
        
        