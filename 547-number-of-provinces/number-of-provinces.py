class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        parent =[i for i in range(n)]
        rank=[0]*n

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            rootX,rootY=find(x),find(y) 
            if rootX==rootY:
                return
            elif rank[rootX]<rank[rootY]:
                parent[rootX]=rootY
            elif rank[rootY]<rank[rootX]:
                parent[rootY]=rootX
            else:
                parent[rootY]=rootX
                rank[rootX]+=1
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    union(i,j)

        provinces= len(set(find(i) for i in range(n)))     
        return provinces                                  
        
        