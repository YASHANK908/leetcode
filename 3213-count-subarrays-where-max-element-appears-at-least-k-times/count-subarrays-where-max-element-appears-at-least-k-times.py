class Solution(object):
    def countSubarrays(self, nums, k):
        maxelement=max(nums)
        left=0
        res=0
        n=len(nums)
        count=0
        for right in range(n):
            if nums[right]==maxelement:
                count+=1
            while count>=k:
                res+=n-right
                if nums[left]==maxelement:
                    count-=1
                left+=1
        return res            

        