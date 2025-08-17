class Solution(object):
    def maxSubArray(self, nums):
        currsum=maxsum=nums[0]
        for i in range(1,len(nums)):
            currsum=max(nums[i],currsum+nums[i])
            maxsum= max(maxsum,currsum)
        return maxsum    
        