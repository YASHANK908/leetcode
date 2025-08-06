class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        map_c={}
        map_t={}
        for mc,mt in zip(s,t):
            if mc in map_c and map_c[mc]!=mt:
                return False
            if mt in map_t and map_t[mt]!=mc:
                return False
            map_c[mc]=mt
            map_t[mt]=mc
        return True    
        