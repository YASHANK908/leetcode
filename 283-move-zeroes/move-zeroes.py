class Solution(object):
    def moveZeroes(self, nums):
        left=0
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left]=nums[right]
                left+=1
        for i in range(left,len(nums)):
            nums[i]=0
        return nums            

        