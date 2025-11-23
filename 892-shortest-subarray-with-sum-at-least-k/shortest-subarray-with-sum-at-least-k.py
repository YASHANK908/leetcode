from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        n=len(nums)
        prefix=0
        prefix_sum=[0]*(n+1)
        dq=deque([0])
        res=float('inf')

        for j in range(n):
            prefix+=nums[j]
            prefix_sum[j+1]=prefix

            while dq and prefix_sum[j+1]-prefix_sum[dq[0]]>=k:
                res=min(res,(j+1)-dq[0])
                dq.popleft()
            while dq and prefix_sum[j+1]<=prefix_sum[dq[-1]]:
                dq.pop()
            dq.append(j+1)
        return res if res!=float('inf') else -1
        