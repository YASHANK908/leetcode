class Solution(object):
    def longestOnes(self, nums, k):
        zeroes=0
        n=len(nums)
        left=0
        maxlen=0
        for right in range(n):
            if nums[right]==0:
                zeroes+=1
            while zeroes>k:
                if nums[left]==0:
                    zeroes-=1
                left+=1
            if right-left+1>maxlen:
                maxlen=right-left+1
        return maxlen
 