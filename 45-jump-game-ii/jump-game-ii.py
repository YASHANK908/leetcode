class Solution(object):
    def jump(self, nums):
        if len(nums)<=1:
            return 0
        jump=0
        f=0
        e=0
        for i in range(len(nums)-1):
            f= max(f,nums[i]+i)
            if i==e:
                jump+=1
                e=f
        return jump    
        