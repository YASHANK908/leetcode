class Solution(object):
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        maxnum=max(nums)
        earn=[0]*(maxnum+1)
        for num in nums:
            earn[num]+=num
        dp=[0]*(maxnum+1)        
        dp[0]=earn[0]
        dp[1]=max(earn[0],earn[1])
        for i in range(2,maxnum+1):
            dp[i]=max(dp[i-1],dp[i-2]+earn[i])
        return dp[maxnum]    