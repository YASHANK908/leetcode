class Solution(object):
    def hIndex(self, citations):
        citations.sort(reverse=True)
        h=0
        for i,c in enumerate(citations,1):
            if c>=i:
                h=i
            else:
                break
        return h            
        
        
        