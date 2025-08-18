class Solution(object):
    def maxChunksToSorted(self, arr):
        n=len(arr)
        prefixmax=[0]*n
        suffixmin=[0]*n

        prefixmax[0]=arr[0]
        for i in range(1,n):
            prefixmax[i]=max(arr[i],prefixmax[i-1])
        suffixmin[-1]=arr[-1]
        for i in range(n-2,-1,-1):
            suffixmin[i]= min(arr[i],suffixmin[i+1])    
        chunks=0
        for i in range(n-1):
            if prefixmax[i]<=suffixmin[i+1]:
                chunks+=1
        return chunks + 1        