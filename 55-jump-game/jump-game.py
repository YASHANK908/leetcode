class Solution(object):
    def canJump(self, nums):
         maxjump=0
         for i in range(len(nums)):
            if i>maxjump:
                return False
            maxjump=max(maxjump,nums[i]+i)
         return True        
        