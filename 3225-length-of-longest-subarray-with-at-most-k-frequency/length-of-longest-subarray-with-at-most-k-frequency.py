from collections import defaultdict
class Solution(object):
    def maxSubarrayLength(self, nums, k):
        freq=defaultdict(int)
        left=0
        maxlen=0
        n=len(nums)
        for right in range(n):
            freq[nums[right]]+=1
            while freq[nums[right]]>k:
                freq[nums[left]]-=1
                left+=1
            
            maxlen =max(maxlen,right-left+1)
        return maxlen