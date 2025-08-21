class Solution(object):
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x:(x[0],-x[1]))
        count=0
        prevend=0
        for _,end in intervals:
            if end>prevend:
                count+=1
                prevend=end
        return count        
        