inf = float('inf')
class Solution(object):
    def minimumArea(self, grid):
        m, n = len(grid), len(grid[0])
        top, left = inf, inf
        bottom, right = -1, -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    top = min(top, i)
                    left = min(left, j)
                    bottom = max(bottom, i)
                    right = max(right, j)

        return 0 if bottom == -1 else (bottom - top + 1) * (right - left + 1)
        