class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        if n==k:
            return sum(cardPoints)
        total=sum(cardPoints)
        windowsize=n-k
        currsum=sum(cardPoints[:windowsize])
        minsum=currsum
        for i in range(windowsize,n):
            currsum+=cardPoints[i]-cardPoints[i-windowsize]
            minsum=min(minsum,currsum)
        return total-minsum
        