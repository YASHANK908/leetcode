class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        res=0
        lastinvalid=-1
        lastmin=lastmax=-1

        for i,num in enumerate(nums):
            if num<minK or num>maxK:
                lastinvalid=i
                lastmin,lastmax=-1,-1
            if num==minK:
                lastmin=i
            if num==maxK:
                lastmax=i
            if lastmin!=-1 and lastmax!=-1:
                res+=max(0,min(lastmin,lastmax)-lastinvalid)
        return res   
 