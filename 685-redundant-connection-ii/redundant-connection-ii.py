class UnionFind:
    def  __init__(self,n):
        self.parent=list(range(n+1))
         
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x]) 
        return self.parent[x]
    def union(self,x,y):
        px,py=self.find(x),self.find(y)
        if px==py:
            return False
        self.parent[py]=px 
        return True 
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        cand1=cand2=None

        for u,v in edges:
            if parent[v]!=v:
                cand1=[parent[v],v]
                cand2=[u,v]
                break
            parent[v]=u
        uf =UnionFind(n)

        for u,v in edges:
            if [u,v]==cand2:
                continue
            if not uf.union(u,v):
                if not cand1:
                    return [u,v]
                else:
                    return cand1
        return cand2                

        