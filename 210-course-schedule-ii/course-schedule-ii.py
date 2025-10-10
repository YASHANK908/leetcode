from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        inDegree=[0]*numCourses

        for u,v in prerequisites:
            graph[v].append(u)
            inDegree[u]+=1

        q= deque([i for i in range(numCourses) if inDegree[i]==0])
        order=[]

        while q:
            course=q.popleft() 
            order.append(course)
            for nei in graph[course]:
                inDegree[nei]-=1
                if inDegree[nei]==0:
                    q.append(nei)
        return order if len(order)==numCourses else []               
        