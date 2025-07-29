class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d={}
        for i,j in enumerate(nums):
            if j in d:
                if abs(i-d[j])<=k:
                    return True
            d[j]=i
        return False
          


         
        