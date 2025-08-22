class Solution(object):
    def countDistinctIntegers(self, nums):
        def reverse(nums):
            rev=0
            while nums>0:
                rev=rev*10+nums%10
                nums//=10
            return rev
        s= set(nums)
        for num in nums:
            s.add(reverse(num))
        return len(s)            
        