class Solution:
    def fib(self, n: int) -> int:
        memo=[-1]*(n+1)
        return self._fib(n,memo)
    
    def _fib(self,n,memo):
            if n==0:
                return 0
            if n==1:
                return 1
            if memo[n]!=-1:
                return memo[n]

            memo[n]=self._fib(n-1,memo)+self._fib(n-2,memo)
            return memo[n]       

             
            

        