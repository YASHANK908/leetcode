class Solution(object):
    def findDuplicate(self, nums):
        n=len(nums)
        low,high=1,n-1
        while low<high:
            mid=(low+high)//2
            count=sum(num<=mid for num in nums)
            if count>mid:
                high=mid
            else:
                low=mid+1
        return low            