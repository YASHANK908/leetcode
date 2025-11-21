from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxdeq=deque()
        mindeq=deque()
        ans=0
        left=0

        for right in range(len(nums)):
            while maxdeq and nums[right]>nums[maxdeq[-1]]:
                maxdeq.pop()
            maxdeq.append(right)

            while mindeq and nums[mindeq[-1]]>nums[right]:
                mindeq.pop()
            mindeq.append(right)

            while nums[maxdeq[0]]-nums[mindeq[0]]>limit:
                if maxdeq[0]==left:
                    maxdeq.popleft()
                if mindeq[0]==left:
                    mindeq.popleft()
                left+=1
            ans=max(ans,right-left+1)
        return ans
            


        
        