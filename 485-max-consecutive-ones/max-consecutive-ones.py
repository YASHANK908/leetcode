class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        res=maxi=0
        for num in nums:
            if num==1:
                res+=1
                maxi=max(maxi,res)
            else:
                res=0
        return maxi            
                
        