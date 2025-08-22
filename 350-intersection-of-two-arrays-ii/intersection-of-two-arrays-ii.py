class Solution(object):
    def intersect(self, nums1, nums2):
        freq={}
        res=[]
        for num in nums1:
            freq[num]=freq.get(num,0)+1
        for num in nums2:
            if num in freq and freq[num]>0:
                res.append(num)
                freq[num]-=1
        return res            

        