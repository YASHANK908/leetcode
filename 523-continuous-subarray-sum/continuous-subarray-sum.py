class Solution(object):
    def checkSubarraySum(self, nums, k):
        runningsum=0
        modmap={0:-1}
        for i,num in enumerate(nums):
            runningsum+=num
            mod=runningsum%k if k!=0 else runningsum
            if mod in modmap:
                if i-modmap[mod]>1:
                    return True
            else:
                modmap[mod]=i
        return False                

        