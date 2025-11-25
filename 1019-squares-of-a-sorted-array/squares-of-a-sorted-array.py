class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        ind=n-1
        left,right=0,n-1

        while left<=right:
            if abs(nums[left])>=abs(nums[right]):
                res[ind]=nums[left]**2
                left+=1
            else:
                res[ind]=nums[right]**2
                right-=1
            ind-=1
        return res

        