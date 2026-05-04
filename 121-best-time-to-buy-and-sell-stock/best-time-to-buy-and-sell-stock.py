class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprofit=prices[0]
        maxprofit=0
        for i in range(1,len(prices)):
            minprofit=min(minprofit,prices[i])
            maxprofit=max(maxprofit,prices[i]-minprofit)
        return maxprofit
        