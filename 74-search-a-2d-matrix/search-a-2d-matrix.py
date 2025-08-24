class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return []
        m,n=len(matrix),len(matrix[0])        
        l,r=0,m*n-1

        while l<=r:
            mid=(l+r)//2
            val=matrix[mid//n][mid%n]
            if val==target:
                return True
            elif val<target:
                l=mid+1
            else:
                r=mid-1
        return False                


        