class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        count={}

        for num in nums:
            count[num]=count.get(num,0)+1
        
        unique=[]
        for num in nums:
            if count[num]==1:
                unique.append(num)
        return sum(unique)
        