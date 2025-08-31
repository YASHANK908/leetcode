class Solution(object):
    def countPrimes(self, n):
        if n<2:
            return 0
        isprimes=[True]*n
        isprimes[0]=isprimes[1]=False

        for i in range(2,int(n**0.5)+1):
            if isprimes[i]:
                for j in range(i*i,n,i):
                    isprimes[j]=False
        return sum(isprimes)                

        