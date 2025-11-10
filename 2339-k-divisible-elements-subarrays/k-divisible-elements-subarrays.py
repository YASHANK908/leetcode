class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        seen = set()   
        
        for left in range(n):
            count_div = 0
            curr = []
            
            for right in range(left, n):
                curr.append(nums[right])
                
                if nums[right] % p == 0:
                    count_div += 1
                
                 
                if count_div > k:
                    break
                
                 
                seen.add(tuple(curr))
        
        return len(seen)