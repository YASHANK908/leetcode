from collections import deque
class Solution(object):
    def maxAreaOfIsland(self, grid):
        rows,cols=len(grid),len(grid[0])
        def bfs(r,c):
            q=deque()
            q.append((r,c))

            grid[r][c]=0
            area=1

            while q:
                row,col=q.popleft()
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc=row+dr,col+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]="0"
                        q.append((nr,nc))
                        area+=1
            return area
        maxarea=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    maxarea=max(maxarea,bfs(r,c))
        return maxarea             



        