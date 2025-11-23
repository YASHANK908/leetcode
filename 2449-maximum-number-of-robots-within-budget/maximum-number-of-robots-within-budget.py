from collections import deque
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n=len(chargeTimes)
        left=0
        sum=0
        ans=0
        dq=deque()
        for right in range(n):
            sum+=runningCosts[right]

            while dq and chargeTimes[dq[-1]]<=chargeTimes[right]:
                dq.pop()
            dq.append(right)

            while dq and (chargeTimes[dq[0]]+(right-left+1)*sum)>budget:
                sum-=runningCosts[left]
                if dq[0]==left:
                    dq.popleft()
                left+=1
            ans=max(ans,right-left+1)    
        return ans
        