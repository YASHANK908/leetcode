class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        pr_sum=0
        count=0

        for i in range(len(nums)):
            pr_sum+=nums[i]
            if pr_sum-k in hashmap:
                count+=hashmap[pr_sum-k]
            hashmap[pr_sum]=hashmap.get(pr_sum,0)+1
        return count
        