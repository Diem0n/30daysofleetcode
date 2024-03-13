class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price_to_buy = 99999
        n = len(prices)
        for i in range(n):
            if prices[i] < min_price_to_buy:
                min_price_to_buy= prices[i]
            else:
                profit = max(prices[i]-min_price_to_buy , profit)
        return profit