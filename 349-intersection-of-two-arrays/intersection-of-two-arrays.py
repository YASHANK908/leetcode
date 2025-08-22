class Solution(object):
    def intersection(self, nums1, nums2):
        s1=set(nums1)
        s=set()
        for num in nums2:
            if num in s1:
                s.add(num)
        return list(s)        
        
        
        