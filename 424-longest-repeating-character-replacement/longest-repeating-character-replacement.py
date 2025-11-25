class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        maxfreq=0
        maxlen=0
        left=0
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            maxfreq=max(maxfreq,freq[s[right]])
            while (right-left+1)-maxfreq>k:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen
        