class Solution(object):
    def waysToSplitArray(self, nums):
        total=sum(nums)
        leftsum=0
        count=0
        n=len(nums)
        for i in range(n-1):
            leftsum+=nums[i]
            rightsum=total-leftsum
            if leftsum>=rightsum:
                count+=1
        return count        