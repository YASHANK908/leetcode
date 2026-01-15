class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0:
                return 0
            
            gold_now=grid[r][c]
            grid[r][c]=0

            up=dfs(r-1,c)
            down=dfs(r+1,c)
            left=dfs(r,c-1)
            right=dfs(r,c+1)

            grid[r][c]=gold_now

            return gold_now +max(up,down,left,right)
        max_gold=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]>0:
                    max_gold=max(max_gold,dfs(r,c))
        return max_gold
        