class Solution(object):
    def maxSubarraySumCircular(self, nums):
        def kadane(nums):
            currsum=maxsum=nums[0]
            for i in range(1,len(nums)):
                currsum=max(nums[i],currsum+nums[i])
                maxsum=max(maxsum,currsum)
            return maxsum
        maxkadane=kadane(nums)
        total=sum(nums)
        minkadane = kadane([-num for num in nums])
        circularsum=total+minkadane
        if circularsum==0:
            return maxkadane
        return max(circularsum,maxkadane)            
        