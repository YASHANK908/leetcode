class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[]
        current=intervals[0]

        for nextinterval in intervals[1:]:
            if nextinterval[0]<=current[1]:
                current[1]=max(current[1],nextinterval[1])
            else:
                ans.append(current)
                current=nextinterval
        ans.append(current)
        return ans
        