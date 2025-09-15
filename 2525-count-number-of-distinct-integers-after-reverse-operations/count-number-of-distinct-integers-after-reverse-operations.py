class Solution(object):
    
    def countDistinctIntegers(self, nums):
        def remove_duplicates(nums):
            i=0
            for j in range(1,len(nums)):
                if nums[j]!=nums[i]:
                    i+=1
                    nums[i]=nums[j]
            return i+1     
        rev_num=[int(str(x)[::-1]) for x in nums]
        allnums=nums+rev_num
        allnums.sort()
        length=remove_duplicates(allnums)
        return length
        
        
        