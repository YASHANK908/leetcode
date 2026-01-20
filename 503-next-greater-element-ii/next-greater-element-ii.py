class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[-1]*n
        stack=[]

        for i in range(2*n):
            idx=i%n
            while stack and nums[idx]>nums[stack[-1]]:
                topidx=stack.pop()
                ans[topidx]=nums[idx]
            if i<n:
                stack.append(idx)
        return ans
        