class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        path=[]

        def dfs(start,k_left,sum_left):
            if sum_left==0 and k_left==0:
                res.append(path.copy())
                return
            
            if k_left<0 or sum_left<0:
                return
            for i in range(start,10):
                if i>sum_left:
                    break
                path.append(i)
                dfs(i+1,k_left-1,sum_left-i)
                path.pop()
        dfs(1,k,n)
        return res
        