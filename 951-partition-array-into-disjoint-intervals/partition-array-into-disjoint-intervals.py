class Solution(object):
    def partitionDisjoint(self, nums):
        n=len(nums)
        prefixmax=[0]*n
        suffixmin=[0]*n

        prefixmax[0]=nums[0]
        for i in range(1,n):
            prefixmax[i]=max(nums[i],prefixmax[i-1])
        suffixmin[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            suffixmin[i]= min(nums[i],suffixmin[i+1])    
         
        for i in range(n-1):
            if prefixmax[i]<=suffixmin[i+1]:
                return i+1
        return n        
        