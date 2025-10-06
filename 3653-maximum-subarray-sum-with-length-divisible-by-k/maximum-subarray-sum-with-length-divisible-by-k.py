class Solution(object):
    def maxSubarraySum(self, nums, k):
        def true_mod(x, k):
            return ((x % k) + k) % k   # normalize remainder
        prefix=0
        minprefix={0:0 } 
        maxsum= float('-inf')
        for i,num in enumerate(nums): 
            prefix += num
             
            r = (i + 1) % k  
             
            
            if r in minprefix: 
                candidate= prefix-minprefix[r]
                maxsum=max(maxsum,candidate)
                 
            
            else: 
                minprefix[r]=prefix
            minprefix[r] = min(minprefix.get(r, float('inf')), prefix)    
        return maxsum        
            
         