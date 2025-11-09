class Solution:
    def countSubarrays(self, nums: List[int], k: int) ->int:
        max_val=max(nums)
        count_max=0
        n=len(nums)
        ans=0
        left=0
        for right in range(n):
            if nums[right]==max_val:
                count_max+=1
            while count_max>=k:
                ans+=(n-right)
                if nums[left]==max_val:
                    count_max-=1
                left+=1
        return ans


        
    