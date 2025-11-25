class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)

        closetsum=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                Sum=nums[i]+nums[left]+nums[right]
                if abs(Sum-target)<abs(closetsum-target):
                    closetsum=Sum
                if Sum<target:
                    left+=1
                elif Sum>target:
                    right-=1
                else:
                    return Sum
        return closetsum    



        