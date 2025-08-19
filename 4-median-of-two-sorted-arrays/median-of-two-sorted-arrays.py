class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        total=m+n
        half=(total+1)//2

        low,high=0,m
        while low<=high:
            i=(low+high)//2
            j=half-i

            aleft=nums1[i-1] if i>0 else float('-inf')
            aright=nums1[i] if i<m else float('inf')
            bleft=nums2[j-1] if j>0 else float('-inf')
            bright=nums2[j] if j<n else float('inf')
            if aleft<=bright and bleft<=aright:
                if total%2==1:
                    return  max(aleft,bleft)   
                return (max(aleft,bleft)+min(aright,bright))/2.0
            elif aleft>bright:
                high=i-1
            else:
                low=i+1        