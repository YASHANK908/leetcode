class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s=set()
        left=0
        Sum=0
        maxsum=0
        for right in range(len(nums)):
            while nums[right] in s:
                s.remove(nums[left])
                Sum-=nums[left]
                left+=1
                
            s.add(nums[right])
            Sum+=nums[right]
            maxsum=max(maxsum,Sum)
            
        return maxsum        
        