class Solution(object):
    def minScoreTriangulation(self, values):
        n = len(values)
        dp = [[0]*n for _ in range(n)]
        
        for l in range(2, n):
            for i in range(n-l):
                j = i + l
                dp[i][j] = float('inf')
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], values[i]*values[k]*values[j] + dp[i][k] + dp[k][j])
        
        return dp[0][n-1]

        