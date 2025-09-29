class Solution(object):
    def rearrangeArray(self, nums):
        i,j=0,1
        n=len(nums)
        res=[0]*len(nums)
        for num in nums:
            if num>0:
                res[i]=num
                i+=2
            elif num<0:
                res[j]=num
                j+=2

           
        return res    
         