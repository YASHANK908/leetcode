class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        merged=[]
        newinterval=intervals[0]
        merged.append(newinterval)
        for interval in intervals:
            if(interval[0]<=newinterval[1]):
                newinterval[1]=max(interval[1],newinterval[1])
            else:
                newinterval=interval
                merged.append(newinterval)
        return merged    
        