class Solution(object):
    def sumSubarrayMins(self, arr):
        mod=10**9+7
        n=len(arr)
        ple=[0]*n
        stack=[]
        for i in range(n):
            count=1
            while stack and arr[i]<stack[-1][0]:
                count+=stack.pop()[1]
            ple[i]=count
            stack.append((arr[i],count))
        nle=[0]*n
        stack=[]
        for i in range(n-1,-1,-1):
            count=1
            while stack and arr[i]<=stack[-1][0]:
                count+=stack.pop()[1]
            nle[i]=count
            stack.append((arr[i],count))

        res=0
        for i in range(n):
            res+=arr[i]*ple[i]*nle[i]   
            res%=mod
        return res             
        