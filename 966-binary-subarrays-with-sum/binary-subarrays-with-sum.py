class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        prefixsum=0
        hashmap={0:1}
        count=0
        for num in nums:
            prefixsum+=num
            if prefixsum-goal in hashmap:
                count+=hashmap[prefixsum-goal]
            hashmap[prefixsum]=hashmap.get(prefixsum,0)+1
        return count    
        