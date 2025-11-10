class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lastinvalid,lastmax,lastmin=-1,-1,-1
        ans=0
        for i in range(len(nums)):
            if nums[i]<minK or nums[i]>maxK:
                lastinvalid=i
                
            if nums[i]==minK:
                lastmin=i
            if nums[i]==maxK:
                lastmax=i

            if lastmin!=-1 and lastmin!=-1:
                ans+=max(0,min(lastmax,lastmin)-lastinvalid)
        return ans             
        