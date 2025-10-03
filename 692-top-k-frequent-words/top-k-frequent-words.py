import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        freq=Counter(words)
        heap=[(-count,word) for word,count in freq.items()]
        heapq.heapify(heap)

        result=[]
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result    



        