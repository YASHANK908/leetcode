class Solution(object):
    def countPairs(self, nums, target):
        nums.sort()
        count=0
        i,j=0,len(nums)-1
        while i<j:
            Sum=nums[i]+nums[j]
            if Sum<target:
                count+=(j-i)
                i+=1
            else:
                j-=1
        return count            
                     
        