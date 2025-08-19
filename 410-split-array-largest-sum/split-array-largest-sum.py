class Solution(object):
    def splitArray(self, nums, k):
        def cansplit(nums,k,mid):
            count=1
            currsum=0
            for num in nums:
                if currsum+num>mid:
                    count+=1
                    currsum=num
                else:
                    currsum+=num
            return count<=k
        low,high=max(nums),sum(nums)
        while low<high:
            mid=(low+high)//2
            if cansplit(nums,k,mid):
                high=mid
            else:
                low=mid+1
        return low                           
        