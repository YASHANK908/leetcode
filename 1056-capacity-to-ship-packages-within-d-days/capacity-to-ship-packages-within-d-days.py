class Solution(object):
    def shipWithinDays(self, weights, days):
        low,high=max(weights),sum(weights)
        while low<high:
            mid=(low+high)//2
            curr=0
            d=1
            for w in weights:
                if curr+w>mid:
                    d+=1
                    curr=w
                else:
                    curr+=w
            if(d<=days):
                high=mid
            else:
                low=mid+1
        return low                        
        