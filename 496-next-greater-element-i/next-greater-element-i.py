class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge={}
        stack=[]

        for current in nums2:
            while stack and current>stack[-1]:
                smaller=stack.pop()
                nge[smaller]=current
            stack.append(current)
        while stack:
            nge[stack.pop()]=-1
        
        return [nge[x] for x in nums1]
        