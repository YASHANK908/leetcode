from collections import deque
class Solution(object):
    def longestSubarray(self, nums, limit):
        left=0
        res=0
        maxd=deque()
        mind=deque()

        for right,num in enumerate(nums):
            while maxd and nums[maxd[-1]]<num:
                maxd.pop()
            maxd.append(right)

            while mind and nums[mind[-1]]>num:
                mind.pop() 
            mind.append(right)     

            while nums[maxd[0]]-nums[mind[0]]>limit:
                left+=1
                if maxd[0]<left:
                    maxd.popleft()
                if mind[0]<left:
                    mind.popleft()
            res =max(res,right-left+1)
        return res      


        