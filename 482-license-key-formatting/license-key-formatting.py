class Solution(object):
    def licenseKeyFormatting(self, s, k):
        cleaned =[c.upper() for c in s if c!="-"]
        if not cleaned:
            return ""
        n= len(cleaned)
        firstlen=n%k
        res=[]
        i=0
        if firstlen>0:
            res.append("".join(cleaned[:firstlen]))
            i=firstlen

        while i<n:
            res.append("".join(cleaned[i:i+k]))
            i+=k
        return "-".join(res)    