class Solution(object):
    def minSwaps(self, nums):
        n= len(nums)
        k= sum(nums)
        windowones=sum(nums[:k])
        maxones=windowones
        for i in range(1,n):
            windowones=windowones-nums[i-1]+nums[(i+k-1)%n]
            maxones=max(maxones,windowones)
        return k-maxones    
        