class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        temp= sorted(nums,reverse=True)
        topk=temp[:k]

        freq={}
        for x in topk:
            freq[x]=freq.get(x,0)+1
        
        ans=[]
        for x in nums:
            if x in freq and freq[x]>0:
                ans.append(x)
                freq[x]-=1
        return ans
    
        