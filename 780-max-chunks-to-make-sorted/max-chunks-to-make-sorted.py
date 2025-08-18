class Solution(object):
    def maxChunksToSorted(self, arr):
        prefixmax=0
        chunks=0
        n=len(arr)

        for i in range(n):
            prefixmax=max(prefixmax,arr[i])
            if i==prefixmax:
                chunks+=1
        return chunks        