from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n=len(nums)
        if n*k==0:
            return []
        q=deque()
        res=[]
        for i in range(n):
            while q and q[0]<i-k+1:
                q.popleft()
            while q and nums[i]> nums[q[-1]]:
                q.pop()        
            q.append(i)

            if i>=k-1:
                res.append(nums[q[0]])
        return res            
        