class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total=3*(1<<(n-1))

        if k>total:
            return ""
        res=[]
        chars=['a','b','c']

        for i in range(n):
            block=1<<(n-i-1)
            for c in chars:
                if res and c==res[-1]:
                    continue
                if k>block:
                    k-=block
                else:
                    res.append(c)
                    break
        return "".join(res)
        