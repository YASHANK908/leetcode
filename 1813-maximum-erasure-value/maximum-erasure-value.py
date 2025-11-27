class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        freq={}
        Sum=0
        maxsum=0
        left=0
        for right in range(len(nums)):
            while nums[right] in freq:
                Sum-=nums[left] 
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    del freq[nums[left]]
                left+=1
            freq[nums[right]]=1
            Sum+=nums[right]
            maxsum=max(maxsum,Sum)
        return maxsum
            
            
        