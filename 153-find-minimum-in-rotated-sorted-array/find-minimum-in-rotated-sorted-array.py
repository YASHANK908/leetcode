class Solution(object):
    def findMin(self, nums):
        n=len(nums)
        low,high=0,n-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
        return nums[low]            
        