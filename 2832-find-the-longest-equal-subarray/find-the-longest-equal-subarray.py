from collections import defaultdict
class Solution(object):
    def longestEqualSubarray(self, nums, k):
        # freq=Counter()
        # maxfreq=0
        # res=0
        # left=0
        # for right in range(len(nums)):
        #     freq[nums[right]]+=1
        #     if freq[nums[right]]>maxfreq:
        #         maxfreq=freq[nums[right]]
        #     while (right-left+1)-maxfreq>k:
        #         freq[nums[left]]-=1
        #         left+=1
        # return maxfreq
                        
        maxf = i = 0
        count = Counter()
        for j in range(len(nums)):
            count[nums[j]] += 1
            maxf = max(maxf, count[nums[j]])
            if j - i + 1 - maxf > k:
                count[nums[i]] -= 1
                i += 1
        return maxf