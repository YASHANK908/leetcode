class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq={}
        maxlen=0
        left=0

        for right in range(len(nums)):
            freq[nums[right]]=freq.get(nums[right],0)+1
            while freq[nums[right]]>k:
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    del freq[nums[left]]
                left+=1
            maxlen=max(maxlen,right-left+1) 
        return maxlen           
        