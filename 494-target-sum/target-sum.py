class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)

        if total<abs(target):
            return 0
        if (total+target)%2==1:
            return 0
        new_target=(total+target)//2
        dp=[0]*(new_target+1)
        dp[0]=1
        for num in nums:
            for s in range(new_target,num-1,-1):
                dp[s]+=dp[s-num]
        return dp[new_target]
                 
        