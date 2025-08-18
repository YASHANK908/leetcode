class Solution(object):
    def jump(self, nums):
        end=0
        jumps=0
        farthest=0
        n=len(nums)
        for i in range(n-1):
            farthest=max(farthest,i+nums[i])
            if i == end:
                jumps+=1
                end=farthest
        return jumps 
             
