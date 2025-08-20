class Solution(object):
    def maximumUniqueSubarray(self, nums):
        left=0
        currsum=0
        maxsum=0
        seen=set()
        n=len(nums)
        for right in range(n):
            while nums[right] in seen:
                seen.remove(nums[left])
                currsum-=nums[left]
                left+=1
            seen.add(nums[right])
            currsum+=nums[right]
            maxsum=max(maxsum,currsum)
        return maxsum    

        