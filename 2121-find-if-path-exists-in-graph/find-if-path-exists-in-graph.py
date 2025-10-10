class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph= [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited=[False]*n

        def dfs(node):
            if node == destination:
                return True
            visited[node]=True
            for nei in graph[node]:
                if not visited[nei] and dfs(nei):
                    return True
            return False
        return dfs(source)                

        