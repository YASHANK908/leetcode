class Solution(object):
    def minSubArrayLen(self, target, nums):
        minlen =float('inf')
        l=0
        cs=0
        for right in range(len(nums)):
            cs+=nums[right]
            while cs>=target and l<=right:
                minlen =min(minlen,right-l+1)
                cs-=nums[l]
                l+=1
             
                
        return 0 if minlen== float('inf') else minlen
        