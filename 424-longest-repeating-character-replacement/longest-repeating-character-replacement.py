class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        maxlen=0
        left=0
        maxcount=0

        for right in range(len(s)):
            c=s[right]
            count[c]=count.get(c,0)+1
            maxcount=max(maxcount,count[c])

            while (right-left+1)-maxcount>k:
                count[s[left]]-=1
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen


        