class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        left=0
        maxlen=0

        for right in range(len(s)):
            
            while s[right] in freq:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
            freq[s[right]]=freq.get(s,0)+1
            maxlen=max(maxlen,right-left+1)
        return maxlen
        