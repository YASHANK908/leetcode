class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(nums):
            n=len(nums)
            if n==0:
                return 0
            if n==1:
                return nums[0]
            dp=[0]*n
            dp[0],dp[1]=nums[0],max(nums[0],nums[1])
            for i in range(2,n):
                dp[i]=max(dp[i-1],nums[i]+dp[i-2])
            return dp[-1]

        n=len(nums)
        if n==1:
            return nums[0]
        return max(rob_linear(nums[:-1]),rob_linear(nums[1:]))    

        
        