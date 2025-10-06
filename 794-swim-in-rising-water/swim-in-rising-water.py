import heapq

class Solution(object):
    def swimInWater(self, grid):
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        minHeap = [(grid[0][0], 0, 0)]  # (time, row, col)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited[0][0] = True
        res = 0
        
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            res = max(res, t)
            if r == n-1 and c == n-1:
                return res
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(minHeap, (grid[nr][nc], nr, nc))
