class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit = 0
        sell = 0
        l = 1
        
        while l<len(prices):
            if profit < prices[l] - buy:
                profit= prices[l]-buy
            if prices[l] < buy:
                buy = prices[l]
            l+=1
        return profit

           

        


