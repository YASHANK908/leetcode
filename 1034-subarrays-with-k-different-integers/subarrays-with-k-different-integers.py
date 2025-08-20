from collections import defaultdict
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atmost(k):
            count=defaultdict(int)
            left=0
            res=0
            n= len(nums)
            for right in range(n):
                if count[nums[right]]==0:
                    k-=1
                count[nums[right]]+=1
                while k<0:
                    count[nums[left]]-=1
                    if count[nums[left]]==0:
                        k+=1
                    left+=1
                res+=right-left+1
            return res
        return atmost(k)-atmost(k-1)                

        