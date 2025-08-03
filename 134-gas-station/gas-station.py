class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n= len(gas)
        start=0
        total=0
        cur_sum=0
        for i in range(n):
            total+=gas[i]-cost[i]
            cur_sum+=gas[i]-cost[i]
            if cur_sum<0:
                start=i+1
                cur_sum=0
        return start if total>=0 else -1

    
    
        