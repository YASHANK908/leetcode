class Solution(object):
    def findClosestElements(self, arr, k, x):
        n=len(arr)
        left,right=0,n-k
        while left<right:
            mid=(left+right)//2
            if x-arr[mid]>arr[mid+k]-x:
                left=mid+1
            else:
                right=mid
        return arr[left:left+k]            
        