class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows,cols=len(grid2),len(grid2[0])

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return True
            if grid2[r][c]==0:
                return True
            
            is_valid=grid1[r][c]==1

            grid2[r][c]=0

            is_valid &=dfs(r+1,c)
            is_valid &=dfs(r-1,c)
            is_valid &=dfs(r,c+1)
            is_valid &=dfs(r,c-1)
            
            return is_valid
        
        count=0

        for r in range(rows):
            for c in range(cols):
                if grid2[r][c]==1:
                    if dfs(r,c):
                        count+=1
        return count
    


        