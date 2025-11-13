class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total=sum(nums)
        target=total-x

        if target<0:
            return -1
        if target==0:
            return len(nums)

        left=0
        right=0
        maxlen=-1
        Sum=0

        for right in range(len(nums)):
            Sum+=nums[right]
            while Sum>target:
                Sum-=nums[left]
                left+=1
            if Sum==target:
                maxlen=max(maxlen,right-left+1)
        return -1 if maxlen==-1 else len(nums)-maxlen        

        