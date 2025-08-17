class Solution(object):
    def numberOfSubarrays(self, nums, k):
        prefixodd=0
        hashmap={0:1}
        result=0

        for num in nums:
            prefixodd+=num%2
            if prefixodd-k in hashmap:
                result+=hashmap[prefixodd-k]
            hashmap[prefixodd]=hashmap.get(prefixodd,0)+1
        return result    

        