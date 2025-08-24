class Solution(object):
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []
        res=[]
        m,n=len(mat),len(mat[0])
        up=True
        i=j=0
        for _ in range(m*n):
            res.append(mat[i][j])
            if up:
                if j==n-1:
                    i+=1
                    up=False
                elif i==0:
                    j+=1
                    up=False
                else:
                    i-=1
                    j+=1
            else:
                if i==m-1:
                    j+=1
                    up=True
                elif j==0:
                    i+=1
                    up=True
                else:
                    i+=1
                    j-=1                        
        return res