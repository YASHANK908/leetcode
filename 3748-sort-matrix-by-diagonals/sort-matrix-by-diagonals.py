from collections import defaultdict

class Solution(object):
    def sortMatrix(self, grid):
        if not grid or not grid[0]:
            return grid

        m, n = len(grid), len(grid[0])
        diags = defaultdict(list)

        
        for i in range(m):
            for j in range(n):
                diags[i - j].append(grid[i][j])

        
        for k, arr in diags.items():
            if k >= 0:
                arr.sort()               
            else:
                arr.sort(reverse=True)   

        # fill back
        for i in range(m):
            for j in range(n):
                grid[i][j] = diags[i - j].pop()

        return grid