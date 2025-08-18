class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        minlen=float('inf')
        n=len(nums)
        currsum=0
        for right in range(n):
            currsum+=nums[right]
            while currsum>=target:
                if right-left+1<minlen:
                    minlen=right-left+1
                currsum-=nums[left]
                left+=1
        return 0 if minlen==float('inf') else minlen            

         