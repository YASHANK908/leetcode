class Solution(object):
    def maxProfit(self, prices):
        minprice=prices[0]
        maxprofit=0
        for i in range(1,len(prices)):
            maxprofit=max(maxprofit,prices[i]-minprice)
            minprice=min(minprice,prices[i])
        return maxprofit    

        