class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total=sum(gas)-sum(cost)
        n=len(gas)
        if total<0:
            return -1
        tank=0
        start=0
        for i in range(n):
            tank+=gas[i]-cost[i]
            if tank<0:
                start=i+1
                tank=0
        return start        
               
         