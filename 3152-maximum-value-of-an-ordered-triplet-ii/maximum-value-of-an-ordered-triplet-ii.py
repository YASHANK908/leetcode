class Solution(object):
    def maximumTripletValue(self, nums):
        res=0
        maxnum=0
        maxdiff=0
        for num in nums:
            res=max(res,maxdiff*num)
            maxnum=max(maxnum,num)
            maxdiff=max(maxdiff,maxnum-num)
        return res   
        