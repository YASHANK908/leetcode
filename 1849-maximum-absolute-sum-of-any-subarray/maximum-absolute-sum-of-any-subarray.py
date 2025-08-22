class Solution(object):
    def maxAbsoluteSum(self, nums):
        currentmax=currentmin=0
        maxsum=minsum=0
        for num in nums:
            currentmax=max(num,currentmax+num)
            maxsum=max(maxsum,currentmax)

            currentmin=min(num,currentmin+num)
            minsum=min(minsum,currentmin)
        return max(maxsum,abs(minsum))    
