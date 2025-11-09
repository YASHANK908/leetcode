class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr=[1 if x&1 else 0 for x in nums]
        def atmost(x):
            if x<0:
                return 0
            left=0
            Sum=0
            left=0
            count=0
            for right in range(len(arr)):
                Sum+=arr[right]
                while Sum>x:
                    Sum-=arr[left]
                    left+=1
                count+=(right-left+1)
            return count 
        return atmost(k)-atmost(k-1)       


        