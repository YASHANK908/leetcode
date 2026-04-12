class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(maxsum):
            subarrays=1
            currsum=0
            for num in nums:
                if currsum+num>maxsum:
                    subarrays+=1
                    currsum=num
                else:
                    currsum+=num
            return subarrays<=k
        
        left,right=max(nums),sum(nums)
        ans=right
        while left<=right:
            mid= left+(right-left)//2
            if cansplit(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans

        