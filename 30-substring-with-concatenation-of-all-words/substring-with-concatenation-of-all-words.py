class Solution(object):
    def findSubstring(self, s, words):
        wl=len(words[0])
        windowlen=wl*len(words)
        wc=Counter(words)
        res=[]
        left=0
        for i in range(wl):
            seen={}
            left= i
            for right in range(i,len(s)-wl+1,wl):
                word=  s[right:right+wl] 
                if word not in wc:
                    seen.clear()
                    left=right+wl
                    continue
                
                seen[word]=seen.get(word,0)+1
          
                while seen[word]>wc[word]: 
                    leftword=s[left:left+wl]
                    seen[leftword]-=1
                    left+=wl
                if right+wl - left == windowlen:
                    res.append(left)
        return res          
        