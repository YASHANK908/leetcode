class Solution(object):
    def findUnsortedSubarray(self, nums):
        n= len(nums)
        maxseen,minseen=float('-inf'),float('inf') 
        
        left,right=-1,-2

        for i in range(n):
            if nums[i]<maxseen:
                right=i
            maxseen=max(maxseen,nums[i])    
        for i in range(n-1,-1,-1):
            if nums[i]>minseen:
                left=i
            minseen=min(minseen,nums[i])    
        return right-left+1        