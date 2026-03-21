from collections import deque 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph=[[] for _ in range(numCourses)]

        indegree=[0]*numCourses
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        
        q=deque(i for i in range(numCourses) if indegree[i]==0)

        total=0

        while q:
            course=q.popleft()
            total+=1
            for nextcourse in graph[course]:
                indegree[nextcourse]-=1
                if indegree[nextcourse]==0:
                    q.append(nextcourse)
        return total==numCourses



        