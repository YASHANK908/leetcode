class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        Sum=0
        left=0
        minlen=float('inf')
        for right in range(len(nums)):
            Sum+=nums[right]
            while Sum>=target:
                minlen=min(minlen,right-left+1)
                Sum-=nums[left]
                left+=1
        return 0 if minlen==float('inf') else minlen
        