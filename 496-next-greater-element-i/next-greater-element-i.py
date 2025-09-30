class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=[]
        nge={}
        for num in nums2:
            while stack and num>stack[-1]:
                nge[stack.pop()]=num
            stack.append(num)

        while stack:
            nge[stack.pop()]=-1
        return [nge[x] for x in nums1]        
