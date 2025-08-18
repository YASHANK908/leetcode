class Solution(object):
    def findMaxAverage(self, nums, k):
        windowsum=sum(nums[:k])
        maxsum=windowsum

        for i in range(k,len(nums)):
            windowsum+=nums[i]-nums[i-k]
            if windowsum>maxsum:
                maxsum=windowsum
        return maxsum/float(k)
 