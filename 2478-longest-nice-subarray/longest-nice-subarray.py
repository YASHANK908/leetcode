class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left=0
        maxlen=0
        mask=0

        for right in range(len(nums)):
            while (mask&nums[right])!=0:
                mask^=nums[left]
                left+=1
            mask|=nums[right]
            maxlen=max(maxlen,right-left+1)    
        return maxlen
        