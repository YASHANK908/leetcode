class Solution(object):
    def findMaxLength(self, nums):
        nums=[1 if x==1 else -1 for x in nums ]
        prefixsum=0
        hashmap={0:-1}
        maxlen=0
        for i,num in enumerate(nums):
            prefixsum+=num
            if prefixsum in hashmap:
                maxlen= max(maxlen,i-hashmap[prefixsum])
            else:
                hashmap[prefixsum]=i
        return maxlen            
            