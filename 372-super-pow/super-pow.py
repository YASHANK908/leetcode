MOD = 1337
class Solution(object):
    def superPow(self, a, b):
        def mypow(x,n):
            x%=MOD
            res=1
            while n>0:
                if n%2==1:
                    res=(res*x)%MOD
                x=(x*x)%MOD
                n//=2
            return res     
        res=1
        for digit in b:
            res=mypow(res,10)*mypow(a,digit)%MOD
        return res            
         