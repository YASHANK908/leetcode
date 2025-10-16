class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=set()

        def backtrack(path):
            if len(path)==len(nums):
                res.append(path[:])
            for num in nums:
                if num not in used:
                    used.add(num)
                    path.append(num)
                    backtrack(path)
                    path.pop()
                    used.remove(num)
        backtrack([])
        return res            
        