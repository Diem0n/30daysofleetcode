class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price_to_buy = prices[0]
        n = len(prices)
        for i in prices:
            profit = max(i - min_price_to_buy , profit)
            min_price_to_buy = min(min_price_to_buy , i)
        return profit