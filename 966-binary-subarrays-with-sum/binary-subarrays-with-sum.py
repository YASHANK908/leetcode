class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(x):
            if x<0:
                return 0
            left=0
            Sum=0
            count=0

            for right in range(len(nums)):
                Sum+=nums[right]
                while Sum>x:
                    Sum-=nums[left]
                    left+=1
                count+=(right-left+1) 
            return count  
        return atmost(goal)-atmost(goal-1)     
        