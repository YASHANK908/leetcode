class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum=sum(nums[:k])
        left=0
        max_sum=window_sum

        for right in range(k,len(nums)):
            window_sum=window_sum-nums[left]+nums[right]
            max_sum=max(window_sum,max_sum)
            left+=1
        
        return max_sum/k
        