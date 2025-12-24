class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n=len(arr)
        prefix=[0]*n
        res=[]
        prefix[0]=arr[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]^arr[i]
        
        for l,r in queries:
            if l==0:
                res.append(prefix[r])
            else:
                res.append(prefix[r]^prefix[l-1])
        return res
        