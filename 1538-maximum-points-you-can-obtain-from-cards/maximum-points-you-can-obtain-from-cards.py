class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        if k==n:
            sum(cardPoints)
        windowsize=n-k
        windowsum=sum(cardPoints[:windowsize])
        minwindow=windowsum
        left=0

        for right in range(windowsize,n):
            windowsum+=cardPoints[right]
            windowsum-=cardPoints[left]
            left+=1
            minwindow=min(minwindow,windowsum)
        
        return sum(cardPoints)-minwindow

        