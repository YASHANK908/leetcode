class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        min_sum=threshold*k
        window_sum=sum(arr[:k])
        
        count=0

        if window_sum>=min_sum:
            count+=1
        
        for right in range(k,len(arr)):
            window_sum=window_sum-arr[right-k]+arr[right]

            if window_sum>=min_sum:
                count+=1
        return count

        