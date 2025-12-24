class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n=len(nums)

        ans=0
        for bit in range(31):
            ones=0
            for num in nums:
                if (num>>bit)&1:
                    ones+=1
            zeroes=n-ones
            ans+=ones*zeroes
        return ans
        