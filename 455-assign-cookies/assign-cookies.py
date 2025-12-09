class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        glen=len(g)
        slen=len(s)
        child=0
        cookie=0

        while child<glen and cookie<slen:
            if s[cookie]>=g[child]:
                child+=1
            cookie+=1
        return child

        