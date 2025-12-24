from collections import defaultdict
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cnt=defaultdict(int)
        sum_idx=defaultdict(int)

        px=0
        res=0

        cnt[0]=1
        sum_idx[0]=0

        for i,num in enumerate(arr):
            px^=num
            p=i+1

            res+=cnt[px]*(p-1)-sum_idx[px]

            cnt[px]+=1
            sum_idx[px]+=p
        return res

        