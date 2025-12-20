class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)

        dp=matrix[0][:]

        for i in range(1,n):
            New=[float('inf')]*n
            for j in range(n):
                straight=dp[j]
                left=dp[j-1] if j-1>=0 else float('inf')
                right=dp[j+1] if j+1<n else float('inf')

                New[j]=matrix[i][j]+min(straight,left,right)
            dp=New
        
        return min(dp)
        