class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent=list(range(n))
        size=[1]*n

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return
            if size[px]<size[py]:
                px,py=py,px
            parent[py]=px
            size[px]+=size[py]
        
        for u,v in edges:
            union(u,v)
        
        components=[]

        for i in range(n):
            if parent[i]==i:
                components.append(size[i])
        remaining=n
        ans=0
        for c in components:
            remaining-=c
            ans+=c*remaining
        
        return ans

        