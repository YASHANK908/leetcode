from collections import deque
class Solution(object):
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        n=len(chargeTimes)
        dq=deque()
        runsum=0
        l=0
        res=0
        for r in range(n):
            runsum+=runningCosts[r]
            while dq and chargeTimes[dq[-1]]<chargeTimes[r]:
                dq.pop()
            dq.append(r)

            while dq and(chargeTimes[dq[0]]+(r-l+1)*runsum)>budget:
                if dq[0]==l:
                    dq.popleft()
                runsum-=runningCosts[l] 
                l+=1
            res=max(res,r-l+1)       
        return res        
        
        
        