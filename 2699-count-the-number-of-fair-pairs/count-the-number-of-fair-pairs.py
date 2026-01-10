class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def count_at_most(x):
            left,right=0,len(nums)-1
            count=0

            while left<right:
                if nums[left]+nums[right]<=x:
                    count+=right-left
                    left+=1
                else:
                    right-=1
            return count
        return count_at_most(upper)-count_at_most(lower-1)
        