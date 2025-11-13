class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[-1]*n
        windowsize=2*k+1
        if windowsize>n:
            return res
        windowsum= sum(nums[0:windowsize])
        res[k]=windowsum//windowsize
        
        left=0
        right=windowsize
        for i in range(k+1,n-k):
            windowsum+=nums[right]
            windowsum-=nums[left]
            right+=1
            left+=1
            res[i]=windowsum//windowsize
        return res
    

        