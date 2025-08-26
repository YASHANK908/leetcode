class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        best_d2 = -1      
        best_area = 0      
        for w, h in dimensions:
            d2 = w*w + h*h
            area = w*h
            if d2 > best_d2:
                best_d2 = d2
                best_area = area
            elif d2 == best_d2 and area > best_area:
                best_area = area
        return best_area
        