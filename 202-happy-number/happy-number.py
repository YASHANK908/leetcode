class Solution(object):
    def isHappy(self, n):
        while n!=1 and n!=4:
            sum=0
            while n>0:
                
                dig=n%10
                sum=sum+dig*dig
                n=n//10
            n=sum  
        return n==1
        