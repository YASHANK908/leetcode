class Solution(object):
    def numberOfPairs(self, points):
        
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        ans = 0

        for i in range(n):
            maxY = -10**18   
            xi, yi = points[i]
            for j in range(i+1, n):
                xj, yj = points[j]
                 
                if yj <= yi and yj > maxY:
                    ans += 1
                    maxY = yj

        return ans
