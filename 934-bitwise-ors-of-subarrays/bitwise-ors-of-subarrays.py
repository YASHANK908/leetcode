class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        prev=set()
        ans=set()
        for x in arr:
            curr={x}
            for p in prev:
                curr.add(p|x)
            ans|=curr
            prev=curr
        return len(ans)
        