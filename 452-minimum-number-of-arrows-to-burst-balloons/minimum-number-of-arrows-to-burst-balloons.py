class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key= lambda x:x[1])
        count=1
        aray_pos=points[0][1]
        for start,end in points:
            if start>aray_pos:
                aray_pos=end
                count+=1
        return count       
        