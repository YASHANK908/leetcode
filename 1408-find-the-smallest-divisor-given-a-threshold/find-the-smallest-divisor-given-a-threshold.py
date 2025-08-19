import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low,high=1,max(nums)
        while low<high:
            mid=(low+high)//2
            total=sum(math.ceil(num/float(mid)) for num in nums)
            if total<=threshold:
                high=mid
            else:
                low=mid+1
        return low            
        