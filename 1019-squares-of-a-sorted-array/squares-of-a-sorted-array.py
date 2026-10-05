class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left=0
        right=len(nums)-1
        ans=[]

        nums

        while left<=right:
            a1=nums[left]**2
            a2=nums[right]**2
            if a1>a2:
                ans.append(a1)
                left+=1
            else:
                ans.append(a2)
                right-=1
        return ans[::-1]

        