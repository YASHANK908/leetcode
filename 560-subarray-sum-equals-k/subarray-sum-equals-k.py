class Solution(object):
    def subarraySum(self, nums, k):
        prefixsum=0
        hashmap={0:1}
        count=0
        for num in nums:
            prefixsum+=num
            if prefixsum-k in hashmap:
                count+=hashmap[prefixsum-k]
            hashmap[prefixsum]=hashmap.get(prefixsum,0)+1
        return count    

        