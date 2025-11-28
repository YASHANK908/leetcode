class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(mid):
            currsum=0
            split=1
            for num in nums:
                if currsum+num<=mid:
                    currsum+=num
                else:
                    split+=1
                    currsum=num
            return split<=k
        low,high=max(nums),sum(nums)
        

        while low<high:
            mid=(low+high)//2
        
            if cansplit(mid):
                high=mid
            else:
                low=mid+1

        return low
        