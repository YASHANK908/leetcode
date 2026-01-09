class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        def backtrack(index,parts,path):
            if parts==4:
                if index==len(s):
                    res.append(".".join(path))
                return
            rem_char=len(s)-index
            rem_parts=4-parts

            if rem_char<rem_parts or rem_char>rem_parts*3:
                return
            

            for length in range(1,4):
                if index+length>len(s):
                    break
                segment=s[index:index+length]

                if len(segment)>1 and segment[0]=='0':
                    continue
                if int(segment)>255:
                    continue
                path.append(segment)
                backtrack(index+length,parts+1,path)
                path.pop()
        backtrack(0,0,[])
        return res 
        