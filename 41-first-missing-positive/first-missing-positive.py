class Solution(object):
    def firstMissingPositive(self, nums):
        n=len(nums)
        i=0
        while i<n:
            current_idx=nums[i]-1
            if 1<=nums[i]<=n and nums[i]!=nums[current_idx]:
                nums[i],nums[current_idx]=nums[current_idx],nums[i]
            else:
                i+=1    
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1                
        