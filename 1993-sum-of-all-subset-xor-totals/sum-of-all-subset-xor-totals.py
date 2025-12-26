class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        bit_or=0
        for num in nums:
            bit_or|=num
        return bit_or * (1<<len(nums)-1)

        