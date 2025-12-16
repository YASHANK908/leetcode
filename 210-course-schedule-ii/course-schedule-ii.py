from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]

        indegree=[0]*numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        
        queue=deque()

        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        order=[]
        while queue:
            curr=queue.popleft()
            order.append(curr)

            for nxt in graph[curr]:
                indegree[nxt]-=1
                if indegree[nxt]==0:
                    queue.append(nxt)
        
        return order if len(order)==numCourses else []
            
        

        