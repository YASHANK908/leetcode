class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(opencount,closecount,path):
            if opencount==n and closecount==n:
                res.append(path)
                return
            if opencount<n:
                backtrack(opencount+1,closecount,path+"(")
            if closecount<opencount:
                backtrack(opencount,closecount+1,path+")")
        backtrack(0,0,"")
        return res
        