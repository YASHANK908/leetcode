class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right=max(weights),sum(weights)

        while left<right:
            mid =left+(right-left)//2
            d=1
            curr=0
            for w in weights:
                if curr+w>mid:
                    d+=1
                    curr=w
                else:
                    curr+=w
            if d<=days:
                right=mid
            else:
                left=mid+1
        return left

        