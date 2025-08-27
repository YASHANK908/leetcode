class Solution(object):
    def lengthOfLongestSubstring(self, s):
        window={}
        left=0
        maxlen=0
        for right in range(len(s)):
            if s[right] in window and window[s[right]]>=left:
                left=window[s[right]]+1
            window[s[right]]=right
            maxlen=max(maxlen,right-left+1)

        return maxlen
        