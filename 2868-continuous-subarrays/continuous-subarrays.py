
from collections import deque
class Solution(object):
    def continuousSubarrays(self, nums):
        start=0
        res=0
        maxdeque=deque()
        mindeque=deque()
        
        for end,val in enumerate(nums):
            while maxdeque and nums[maxdeque[-1]]<=val:
                maxdeque.pop()
            maxdeque.append(end)

            while mindeque and nums[mindeque[-1]]>=val:
                mindeque.pop()
            mindeque.append(end)
            
            while nums[maxdeque[0]] -nums[mindeque[0]]>2:
                start+=1
                if maxdeque[0]<start:
                    maxdeque.popleft()
                if mindeque[0]<start:
                    mindeque.popleft()
            res+=end-start+1
        return res                