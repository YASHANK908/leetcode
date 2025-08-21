class Solution(object):
    def getMaxLen(self, nums):
        pos=0
        neg=0
        maxlen=0
        for num in nums:
            if num>0:
                pos+=1
                neg=neg+1 if neg>0 else 0
            elif num<0:
                pos,neg=(neg+1 if neg>0 else 0),pos+1
            else:
                pos=0
                neg=0
            maxlen=max(maxlen,pos)
        return maxlen                   
        
        