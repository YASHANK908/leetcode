class Solution(object):
    def zeroFilledSubarray(self, nums):
        count = 0
        curr = 0
        for num in nums:
            if num == 0:
                curr += 1
                count += curr
            else:
                curr = 0
        return count
        
        