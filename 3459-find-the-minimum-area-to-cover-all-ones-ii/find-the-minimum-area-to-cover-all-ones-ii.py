class Solution(object):
    def minimumSum(self, grid):
        m, n = len(grid), len(grid[0])

        def area(r1, r2, c1, c2):
            minr, maxr, minc, maxc = 10**9, -1, 10**9, -1
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if grid[r][c] == 1:
                        if r < minr: minr = r
                        if r > maxr: maxr = r
                        if c < minc: minc = c
                        if c > maxc: maxc = c
            if maxr == -1:   
                return 0
            return (maxr - minr + 1) * (maxc - minc + 1)

        ans = 10**9

         
        for c1 in range(n - 2):
            for c2 in range(c1 + 1, n - 1):
                a = area(0, m - 1, 0, c1)
                b = area(0, m - 1, c1 + 1, c2)
                c = area(0, m - 1, c2 + 1, n - 1)
                ans = min(ans, a + b + c)

        
        for r1 in range(m - 2):
            for r2 in range(r1 + 1, m - 1):
                a = area(0, r1, 0, n - 1)
                b = area(r1 + 1, r2, 0, n - 1)
                c = area(r2 + 1, m - 1, 0, n - 1)
                ans = min(ans, a + b + c)

         
        for r in range(m - 1):
            for c in range(n - 1):
                
                left_top    = area(0, r, 0, c)
                left_bottom = area(r + 1, m - 1, 0, c)
                right_all   = area(0, m - 1, c + 1, n - 1)
                ans = min(ans, left_top + left_bottom + right_all)

                
                right_top    = area(0, r, c + 1, n - 1)
                right_bottom = area(r + 1, m - 1, c + 1, n - 1)
                left_all     = area(0, m - 1, 0, c)
                ans = min(ans, right_top + right_bottom + left_all)

                
                top_left   = area(0, r, 0, c)
                top_right  = area(0, r, c + 1, n - 1)
                bottom_all = area(r + 1, m - 1, 0, n - 1)
                ans = min(ans, top_left + top_right + bottom_all)

                 
                bottom_left  = area(r + 1, m - 1, 0, c)
                bottom_right = area(r + 1, m - 1, c + 1, n - 1)
                top_all      = area(0, r, 0, n - 1)
                ans = min(ans, bottom_left + bottom_right + top_all)

        return ans
         
        