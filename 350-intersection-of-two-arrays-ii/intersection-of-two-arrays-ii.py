class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count={}
        res=[]
        for num in nums1:
            count[num]=count.get(num,0)+1
        
        for num in nums2:
            if count.get(num,0)>0:
                res.append(num)
                count[num]-=1
        return res
        