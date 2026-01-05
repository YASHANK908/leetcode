class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited=[False]*len(nums)
        res=[]
        def dfs(path):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i]=True
                path.append(nums[i])
                dfs(path)
                path.pop()
                visited[i]=False
        dfs([])
        return res
        