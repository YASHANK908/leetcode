class Solution(object):
    def applyOperations(self, nums):
        n=len(nums)

        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        pos=0
        for i in range(n):
            if nums[i]!=0:
                nums[i],nums[pos]=nums[pos],nums[i]
                pos+=1
        return nums        




        