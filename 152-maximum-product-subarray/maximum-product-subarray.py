class Solution(object):
    def maxProduct(self, nums):
        maxprod=minprod=result=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                maxprod,minprod=minprod,maxprod
            maxprod=max(nums[i],maxprod*nums[i])
            minprod=min(nums[i],minprod*nums[i])
            result=max(result,maxprod)
        return result        
        