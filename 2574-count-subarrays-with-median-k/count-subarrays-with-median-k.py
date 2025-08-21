class Solution(object):
    def countSubarrays(self, nums, k):
        n=len(nums)
        kindex=nums.index(k)
        freq={0:1}
        balance=0

        for i in range(kindex-1,-1,-1):
            balance+=1 if nums[i]>k else -1
            freq[balance]=freq.get(balance,0)+1
        res=0
        balance=0
        for i in range(kindex,n):
            if nums[i]>k:
                balance+=1
            elif nums[i]<k:
                balance-=1
            res+= freq.get(-balance,0)
            res+=freq.get(-balance+1,0)
        return res          
        