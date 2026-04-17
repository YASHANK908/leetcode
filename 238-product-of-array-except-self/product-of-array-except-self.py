class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[1]*n

        suffix=1
        for i in range(n):
            result[i]=suffix
            suffix*=nums[i]
        prefix=1
        for i in range(n-1,-1,-1):
            result[i]*=prefix
            prefix*=nums[i]
        return result        