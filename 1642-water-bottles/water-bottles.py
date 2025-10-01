class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total_drunk = 0
        empty = 0
        
        while numBottles > 0:
            total_drunk += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty = empty % numExchange
            
        return total_drunk
