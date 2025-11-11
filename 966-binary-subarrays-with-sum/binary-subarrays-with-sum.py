class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixmap={0:1}
        count=0
        Sum=0
        for i in range(len(nums)):
            Sum+=nums[i]
            if Sum-goal in prefixmap:
                count+=prefixmap[Sum-goal]
            prefixmap[Sum]=prefixmap.get(Sum,0)+1
        return count        
        