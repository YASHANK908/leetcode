class Solution:
    def triangularSum(self, nums):
        n = len(nums)
        ans = 0
        coeff = 1   
        
        for i in range(n):
            ans = (ans + coeff * nums[i]) % 10
           
            if i < n-1:
                coeff = coeff * (n-1-i) // (i+1)
        return ans

        