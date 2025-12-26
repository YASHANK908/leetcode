import heapq
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m,n=len(matrix),len(matrix[0])
        px=[[0]*(n+1) for _ in range(m+1)]
        heap=[]

        for i in range(m):
            for j in range(n):
                px[i+1][j+1]=(px[i][j+1]^px[i+1][j]^px[i][j]^matrix[i][j])
                val=px[i+1][j+1]

                heapq.heappush(heap,val)
                if len(heap)>k:
                    heapq.heappop(heap)
        return heap[0]

        