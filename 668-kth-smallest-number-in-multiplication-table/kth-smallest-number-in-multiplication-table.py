class Solution(object):
    def findKthNumber(self, m, n, k):
        
        low,high=0,m*n
        def countlessequal(x):
            count=0
            for i in range(1,m+1):
                count+=min(n,x//i)
            return count
       
        while low<high:
            mid=(low+high)//2
            if countlessequal(mid)<k:
                low=mid+1
            else:
                high=mid
        return low                    


