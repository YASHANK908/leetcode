class Solution(object):
    def subarraysDivByK(self, nums, k):
        prefixsum=0
        hashmap={0:1}
        count=0
        for num in nums:
            prefixsum+=num
            mod=prefixsum%k
            if mod<0:
                mod+=k
            if mod in hashmap:
                count+= hashmap[mod]
            hashmap[mod]=hashmap.get(mod,0)+1
        return count            
         