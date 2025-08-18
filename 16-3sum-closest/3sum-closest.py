class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n=len(nums)
        closetsum=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            left,right=i+1,n-1
            while left<right:
                currentsum=nums[i]+nums[left]+nums[right]
                if abs(currentsum-target)<abs(closetsum-target):
                    closetsum=currentsum
                if currentsum<target:
                    left+=1
                elif currentsum>target:
                    right-=1
                else:
                    return currentsum
        return closetsum                        
        