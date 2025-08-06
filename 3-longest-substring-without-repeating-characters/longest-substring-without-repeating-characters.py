class Solution(object):
    def lengthOfLongestSubstring(self, s):
        track={}
        maxlen=0
        left=0
        for right,ch in enumerate(s):
            if ch in track and track[ch]>=left:
                left=track[ch]+1
            track[ch]=right
            maxlen=max(maxlen,right-left+1)
        return maxlen        
        
        
        