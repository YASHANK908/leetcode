class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        parent =[i for i in range(n)]
        rank=[0]*n
        
        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return
            if rank[px]<rank[py]:
                parent[px]=py
            elif rank[py]<rank[px]:
                parent[py]=px
            else:
                parent[py]=px
                rank[px]+=1
        
        for u,v in connections:
            union(u,v)
        
        components=sum(1 for i in range(n) if find(i)==i)

        return components-1


        