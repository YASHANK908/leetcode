class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if len(s1)!=len(s2):
            return False
        diff=[]
        for i in range(len(s1)):
            if(s1[i]!=s2[i]):
                diff.append(i)
        if len(diff)==0:
            return True 
             
        if len(diff)!=2:
            return False
        i,j=diff
        return s1[i]==s2[j] and s1[j]==s2[i]                             
