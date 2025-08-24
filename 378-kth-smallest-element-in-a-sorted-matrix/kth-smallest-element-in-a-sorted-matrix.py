class Solution(object):
    def kthSmallest(self, matrix, k):
        m,n=len(matrix),len(matrix[0])
        low,high=matrix[0][0],matrix[-1][-1]
        def countlessequal(mid):
            count=0
            row,col=m-1,0
            while row>=0 and col<n:
                if matrix[row][col]<=mid:
                    count+=row+1
                    col+=1
                else:
                    row-=1
            return count
        
        
        while low<high:
            mid=(low+high)//2
            if countlessequal(mid)<k:
                low=mid+1
            else:
                high=mid
        return low            
