class Solution(object):
    def maxSubArray(self, nums):
        cs=nums[0]
        maxsum=nums[0]
        for num in nums[1:]:
            cs= max(num,cs+num)
            maxsum=max(maxsum,cs)
        return maxsum   
        