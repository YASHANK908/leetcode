MOD=10**9+7
class Solution(object):
    def countGoodNumbers(self, n):
        def mypow(num,kipower,mod=MOD):
            num%=mod
            res=1
            while kipower>0:
                if kipower&1:
                    res=(res*num)%mod
                num=(num*num)%mod
                kipower>>=1 
            return res   
        even_positions=(n+1)//2
        odd_positions=n//2
        return (mypow(5,even_positions)*mypow(4,odd_positions))%MOD        