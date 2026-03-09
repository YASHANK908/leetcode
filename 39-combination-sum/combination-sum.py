class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(index,curr,remaining):
            if remaining==0:
                res.append(curr[:])
            if remaining<0:
                return
            for i in range(index,len(candidates)):
                curr.append(candidates[i])
                backtrack(i,curr,remaining-candidates[i])
                curr.pop()
        backtrack(0,[],target)
        return res
        