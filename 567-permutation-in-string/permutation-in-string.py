 
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        s1_count=[0]*26
        window=[0]*26
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')]+=1
        for i in range(len(s1)):
            window[ord(s2[i])-ord('a')]+=1
        if window==s1_count:
            return True   

        for i in range(len(s1),len(s2)):
            window[ord(s2[i])-ord('a')]+=1
            window[ord(s2[i-len(s1)])-ord('a')]-=1
            if window==s1_count:
                return True
        return False        


        