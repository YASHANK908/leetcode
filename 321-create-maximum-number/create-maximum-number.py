class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        def pickmax(nums,k):
            stack=[]
            drop=len(nums)-k
            for num in nums:
                while drop and stack and stack[-1]<num:
                    stack.pop()
                    drop-=1
                stack.append(num)   
            return stack[:k]
        def merge(a,b):
            res = []
            i = j = 0
            while i < len(a) or j < len(b):
                if a[i:] > b[j:]:
                    res.append(a[i]); i += 1
                else:
                    res.append(b[j]); j += 1
            return res
        best =[]
        for i in range(max(0,k-len(nums2)),min(k,len(nums1))+1):
            part1=pickmax(nums1,i)
            part2=pickmax(nums2,k-i)
            candidate=merge(part1,part2)
            best=max(best,candidate)
        return best    

        