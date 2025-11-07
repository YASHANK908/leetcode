class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        maxlen=0
        window={}

        for right in range(len(s)):
            if s[right] in window and window[s[right]]>=left:
                left=window[s[right]]+1
            window[s[right]]=right
            maxlen=max(maxlen,right-left+1)    
        return maxlen    
        