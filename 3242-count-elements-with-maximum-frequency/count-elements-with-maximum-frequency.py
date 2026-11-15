class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count={}

        for num in nums:
            count[num]=count.get(num,0)+1
        max_freq=max(count.values())
        result=0
        for num in nums:
            if count[num]==max_freq:
                result+=1
        
        return result