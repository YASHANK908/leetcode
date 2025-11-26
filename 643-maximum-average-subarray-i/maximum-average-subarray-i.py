class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])
        maxav=window_sum/k

        for i in range(k,len(nums)):
            window_sum+=nums[i]-nums[i-k]
            maxav=max(maxav,window_sum/k)
        return maxav