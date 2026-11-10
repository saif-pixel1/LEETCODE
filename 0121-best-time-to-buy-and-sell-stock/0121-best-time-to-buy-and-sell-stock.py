class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit = 0
        sell = 0
        l = 1
        # if len(prices) <2:
        #     return 0
        # if prices[0] > prices[1]:
        #     buy = prices[1]
        #     l = 1
        # else:
        #     buy=prices[0]
        #     l = 0
        # while r<len(prices):

        while l<len(prices):
            if profit < prices[l] - buy:
                profit= prices[l]-buy
            if prices[l] < buy:
                buy = prices[l]

            l+=1
        return profit

           

        


